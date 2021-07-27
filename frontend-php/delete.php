<?php

$api_key = 'sjadhuwhduiahhsjhduwudhjxxgq'; //this is admin (can do anything)
//$api_key = 'shdyegdhzudifhesydahwyeygd'; //this is user (can not update,insert,and delete data)
$api_url = 'http://127.0.0.1:5000/product/'.$api_key;

$id = $_GET['id'];

$data = array(
    'id_product' => $id
);

$curl = curl_init($api_url);
curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
curl_setopt($curl, CURLOPT_CUSTOMREQUEST, "DELETE");
curl_setopt($curl, CURLOPT_POSTFIELDS,  json_encode($data));
curl_setopt($curl, CURLOPT_HTTPHEADER, [
   'Content-Type: application/json'
]);
$response = curl_exec($curl);
$httpcode = curl_getinfo($curl, CURLINFO_HTTP_CODE);
curl_close($curl);

if ($httpcode == 200){
    echo "<script>
            alert('Data has been deleted successfully');
            window.location.href='index.php';
            </script>";
}
else{
    echo "<script>
            alert('Data can not be deleted! Internal Server Error');
            window.location.href='index.php';
            </script>";
}


print_r($data);
?>