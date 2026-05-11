# Use the official slim Python 3.11 image to minimize attack surface and image size
FROM python:3.11-slim

# Set working directory inside the container; all subsequent paths are relative to this
WORKDIR /app

# Create a non-root user and group so the app doesn't run as root
RUN groupadd --gid 1001 appgroup && \
    useradd --uid 1001 --gid appgroup --no-create-home appuser

# Copy only the dependency manifest first — this layer is cached and won't rebuild
# unless requirements.txt changes, even if application code changes
COPY requirements.txt .

# Install dependencies; --no-cache-dir keeps the image lean by skipping pip's cache
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application source code after dependencies are installed
# so that code edits don't invalidate the expensive pip layer above
COPY . .

# Transfer ownership of the app directory to the non-root user
RUN chown -R appuser:appgroup /app

# Switch to the non-root user for all subsequent commands and at runtime
USER appuser

# Declare the port the app listens on (informational; does not publish the port)
EXPOSE 5000

# Run the app with Gunicorn instead of Flask's dev server for production:
#   -w 2     — two worker processes (adjust to match CPU cores)
#   -b       — bind to all interfaces on port 5000
#   --access-logfile - — send access logs to stdout so container runtimes can capture them
CMD ["python", "-m", "gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "--access-logfile", "-", "app:app"]
