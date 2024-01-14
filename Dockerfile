FROM python:3.10-bookworm
RUN pip install Flask
RUN pip install requests
RUN pip install beautifulsoup4
RUN pip install html2text