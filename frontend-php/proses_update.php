<?php

$api_key = 'sjadhuwhduiahhsjhduwudhjxxgq'; //this is admin (can do anything)
//$api_key = 'shdyegdhzudifhesydahwyeygd'; //this is user (can not update,insert,and delete data)
$api_url = 'http://127.0.0.1:5000/product/'.$api_key;

$product_name = $_POST['product_name'];
$product_type = $_POST['product_type'];
$price = $_POST['price'];
$date = $_POST['created_date'];
$id_p = $_POST['id_product'];


$data = array(
    'created' => $date,
    'price'   => $price,
    'product_name' => $product_name,
    'product_type' => $product_type,
    'id_product' => $id_p
);

$curl = curl_init($api_url);
curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
curl_setopt($curl, CURLOPT_CUSTOMREQUEST, "PUT");
curl_setopt($curl, CURLOPT_POSTFIELDS,  json_encode($data));
curl_setopt($curl, CURLOPT_HTTPHEADER, [
   'Content-Type: application/json'
]);
$response = curl_exec($curl);
$httpcode = curl_getinfo($curl, CURLINFO_HTTP_CODE);
curl_close($curl);

if ($httpcode == 200){
    echo "<script>
            alert('Data has been updated successfully');
            window.location.href='index.php';
            </script>";
}
else{
    echo "<script>
            alert('Data can not be updated! Internal Server Error');
            window.location.href='index.php';
            </script>";
}

?>