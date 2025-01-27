FROM python:3.9
WORKDIR /app
COPY . .
CMD ["./dist/add2vals"]