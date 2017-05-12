<=====Register   version 5/11===> 


<======= 5:45 PM ======================= > 



#! /bin/bash

#askMichael


echo "Content-type: text/html"
echo ""



if [[ -n ${QUERY_STRING} ]]; then
function urldecode {
        local url_encoded="${1//+/}"
        printf '%b' "${url_encoded//%/\\x}"
        }

OIFS=$IFS
IFS='=&'
parm_get=($QUERY_STRING)
IFS=$OIFS
        for (( i=0; i<${#parm_get[@]}; i+=2)); do
                        declare var_${parm_get[i]}=$(urldecode ${parm_get[i+1]})
                done

        full=$var_firstname:$var_lastname:$var_usrname:$var_type
        info=$var_usrname:$var_password

        data=1
        credentials=~/public_html/cgi-bin/accountsinfo.txt

        data=$(cat credentials.txt | grep $var_usrname)

        if [[ $data == *"$var_usrname"* ]]; then
                echo "<script>window.alert(\"Username is Registered Already\")</script>"
        else
                echo "$full" >> accountsinfo.txt
                echo "$info" >> accounts.txt
                echo "<script>window.alert(\"Thank you for registering! Please login to continue.\")</script>"
                echo "<meta http-equiv='refresh' content='0; url=http://cit160lab.sandbox.csun.edu/~team11/cgi-bin/' />"
        fi
fi









cat header.html

cat << EOF
<!DOCTYPE html>
<center>
<head>


        <style type="text/css">
                body {
                        background-color:#FAEBD7;
                }
                .header img {
                                float: left;
                                width: 60px;
                                height: 60px;
                        }
                #find out how to import

                        input[type="text"], input[type="password"]{
                        width: 100%
                        padding: 12px 20px;
                        margin: 8px 0;
                        display: inline-block;
                        border: 1px solid #ccc;
                        box-sizing: border-box;
                        font-family: "Roboto",sans serif;
                        font-size:16px;
                }

                #login {
                        padding-right: 4em;
                }

                form {
                        border: 5px solid #0000ff;
                        padding: 12px;
                        margin: 20px;
                 }

                h1, h2 {
                        font-family: "Roboto",sans serif;
                        font-size: 25px;
                        color: blue;
                        padding: 20px;
                }

                label {
                        font-family: "Roboto",sans serif;
                        font-size: 20px;
                        color: red;
                }

                input[type='button'] {
                        font-family: "cursive",sans serif;
                        font-size: 16px;
                        color: red;
                        background-color: blue;
                }


                input[type='submit'] {
                        font-family: "Impact",sans serif;
                        font-size: 25px;
                        color: white;
                        background-color: blue;
                }

                #TestFont {
                font-family: "Roboto",sans serif;
                font-size: 20px;
                color: white;
                }
        </style>



<script type="text/javascript">
                function register() {
                var form = document.getElementsByTagName("form")[0];
                form.innerHTML =
                "<strong><h1>New Account Registration </h1> </strong>" +
                "<br><br>" +
                "<span id=TestFont>First Name: </span><input type='text' name='firstname' id='firstname' size='20' />" +
                "<br><br>" +
                "<span id=TestFont>Last Name:</span><input type='text' name='lastname' id='lastname' size='20' />" +
                "<br><br>" +
                "<span id=TestFont>Username:</span><input type='text' name='usrname' id='usrname' size='20' />" +
                "<br><br>"+
                "<span id=TestFont>Password: </span><input type='password' name='password' id='password' size='20' />" +
                "<br><br>" +
                "<span id=TestFont>I am: </span><select><option value='student'>a Student</option><option value='intructor'>an Intructor</option></select>" +
                "<br><br>" +
                "<input type='button' onclick='register()' value='Register Me' />";
                }
</script>





<form>
<font size="6">
 <strong> Please Register your Account. </strong>
</font>

<br>
<br><br>
<h1>
<span style="color:blue;font-weight:bold">First Name:  </span><input type='text' name='firstname' id='firstname' size='20' />
<span style="color:blue;font-weight:bold">Last Name:  </span><input type='text' name='lastname' id='lastname' size='20' />

</h1>
<br><br>

<h2>
<span style="color:blue;font-weight:bold">Username:  </span><input type='text' name='username' id='username' size='20' />
<img src="http://i.imgur.com/VU2Vozb.png" style="width 220px; height 250px; position: absolute; TOP:14em; LEFT:35em;"   >




</h2>

<h2>

<span style="color:blue;font-weight:bold">Password:  </span><input type='text' name='password' id='password' size='20' />
</h2>
<br><br>

<h2>
<span style="color:blue;font-weight:bold"> Please choose an account type:

<input type="radio" name="option" value="Student">
Student
<input type="radio" name="option" value="Instructor">
Instructor


</h2>

<input type='submit' value="             Register my Account" id="login" />






</form>
</body>
</center
</html>
EOF


cat footer.html



<======================================================================================================>
