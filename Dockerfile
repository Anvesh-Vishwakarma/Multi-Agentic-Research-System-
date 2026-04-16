# Base Image
FROM python:3.10

# WorkdIr
WORKDIR /app

# copy
COPY . /app

# run 
RUN pip install -r requirement.txt

# port
EXPOSE 8501

# Command
CMD ["streamlit", "run", "app.py"]