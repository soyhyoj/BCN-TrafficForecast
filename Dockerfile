# Start base image
FROM jupyter/base-notebook:python-3.7.6

# Copy over requirements
COPY requirements.txt .

# Install requirements. No cache to lower the image size.
RUN pip install --no-cache -r requirements.txt