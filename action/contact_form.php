<?php
include("./connect.php");
$username = $_POST["name"];
$email = $_POST["email"];
$phone = $_POST["phone"];
$Topic_message = $_POST["message"];
$insert="insert into Contact_detailes values('','$username','$email','$phone','$Topic_message')";
$query=mysqli_query($connect,$insert);
if($query){
    echo "<script>
alert('Contact Details Saved Successful');
alert('We will Contact you Soon');
alert('Thank You');
</script>";
}
?>

