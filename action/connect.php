<?php
//domain name,username,password,database_name
$domain_name="gagan.000.pe";
$username="if0_36485657";
$password="SYcJd8EyFNAoA3o";
$database_name="if0_36485657_Contact";
$connect=mysqli_connect($domain_name,$username,$password,"$database_name");
if(!$connect){
    die(mysqli_error($connect));
}
?>