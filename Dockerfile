# import base image 
FROM python:3.10-slim

# create working directory (work folder) to be called app
WORKDIR /app

# copy requirements.txt file to the work folder
COPY requirements.txt .

# execute requirements.txt file to install dependencies
RUN pip install -r requirements.txt

# coopy everything into the work folder
COPY . .

# expose to a particular port
EXPOSE 8501

# run command CMD
CMD ["streamlit", "run", "inference.py"]