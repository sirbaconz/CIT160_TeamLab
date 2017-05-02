====Read only part=======

Created 5/02/2017 1:00am

index.cgi

correct path use of public_html and cgi-bin



========END===============================



#! /bin/bash

echo "Content-type: text/html"
echo ""



cat header.html



cat << EOF



<!DOCTYPE html>
<head>
        <title>Team 11 - Class Solutions</title>
        <style type="text/css">
                body {
                        background-color:       #FAEBD7;
                        color: #0B0B0B;
                }

                h1 {
                        color: #0B0B0B;
                        font-size: 24px;
                }
        </style>
</head>
<body>


<center>

<h1> What is his end game? (place holder logo) </h1>


<img src="http://i.imgur.com/JRdYdqo.png" alt="It's happening" style="width:500; height:750;">


<div class="form">
<form>
<h2>Please Login</h2>
<div class= "container">
<label><b>Username:</b></label>
<input type="text" placeholder="Enter Username" name="username" required>
<br>
<label><b>Password:</b></label>
<input type="password" placeholder="Enter Password" name="password" required>
<br>
<input type="button" value="Log In" onclick="login()">
<input type="button" value="New User?" onclick="register()">


<br>
<input type="radio" name="option" value="Student">
Student
<input type="radio" name="option" value="Instructor">
Instructor
</br>

</center>
</div>
</form>
</body>
</html>
EOF

cat footer.html
