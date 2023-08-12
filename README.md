# Flask_Custom_Images
## 1.Create a Project Directory
Create a project Directory For this Project and change your Directory
      
      mkdir flask
      cd flask
## 2.Flask application:
Create a file named app.py for your Flask application. and write your flask code:

      sudo vim app.py
## 3.requirement.txt
Create a file named requirement.txt for running code

          Flask
## 4.Create a Dockerfile:
Create a Dockerfile in your project directory to define how the Docker image should be built.

        sudo vim Dockerfile
## 5.template:
Create a Directory as your project Directory. and change your Directory. Create a file
in this Directory index.html.

        mkdir template
        cd template
        sudo vim index.html
## 6.static:
Create a Directory in your project Directory name static. and change your Directory . Create a file
style.css

         cd ..
         mkdir static
         sudo vim style.css
## 7.Build Docker Image:
         docker build -t flask-app-9.
## 8.Run the Containers:
          sudo docker run -d -p 1414:5000 flask-app-9:latest
## 9.Access Your Application:
Open a web browser and navigate to http://localhost:1414
