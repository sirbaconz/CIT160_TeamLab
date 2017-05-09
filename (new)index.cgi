====Read only part=======

Created 5/02/2017 1:00am

index.cgi

correct path use of public_html and cgi-bin

Please refer to header.html and footer.html to change global visuals for each page (both are loaded on each page)



========END===============================
Updated 5/9
Nabeel Auth version (changing var names)


#! /bin/bash

echo "Content-type: text/html"
echo ""




function urldecode {
        local url_encoded="${1//+/}"
        printf '%b' "${url_encoded//%/\\x}"
}

OIFS=$IFS
IFS='=&'
parm_get=($QUERY_STRING)
IFS=$OIFS
for (( i=0; i<${#parm_get[@]}; i+=2 )); do
        declare var_${parm_get[i]}=$(urldecode ${parm_get[i+1]})
done

loginid=$var_Username
loginid+=:
loginid+=$var_Password
details=0

if grep -Fxq $loginid database/accounts.txt
then
        details=$(cat database/accountsinfo.txt | grep $var_Username)
        #echo "$details"
        details=7
else

        #echo "$details"
        details+=1
fi



cat header.html



cat << EOF



<!DOCTYPE html>
<head>
EOF

cat << EOF


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


<h1> Login to Class Solutions (edit style pls)  </h1>




<div class="form">
<form>
<div class="container">
<label><b>Username:</b></label>
<input type="text" placeholder="Enter Username" name="username" required>
<br>
<label><b>Password:</b></label>
<input type="password" placeholder="Enter Password" name="password" required>

<br>
<input type="radio" name="option" value="Student">Student
<input type="radio" name="option" value="Instructor">Instructor
<br>
<input type="button" value="Log In" onclick="login()">
<input type="button" value="New User" onclick="window.location.href='registration.cgi'"></br>
</br>

The top buttons won't work until user logins, it'll be the header to
navigate around our "Class Solution" Site

</center>
</div>
</form>
</body>
</html>

EOF

cat footer.html

