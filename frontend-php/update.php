<?php
$id = $_GET['id'];

$api_key = 'shdyegdhzudifhesydahwyeygd'; //this is user (can not update,insert,and delete data)
$api_url = 'http://127.0.0.1:5000/product/'.$api_key.'/'.$id;
 

// Read JSON file
$json_data = file_get_contents($api_url);

// Decode JSON data into PHP array
$response_data = json_decode($json_data);

// All user data exists in 'data' object
$api_data = $response_data->product;

?>

<form action="proses_update.php" method="POST">
Product Name: <input type="text" name="product_name" value="<?= $api_data[0]->name_product  ?>" style="width:350px"><br>
Product Type: <input type="text" name="product_type" value="<?= $api_data[0]->type_product  ?>" ><br>
Price: <input type="text" name="price" value="<?= $api_data[0]->price  ?>"> example (40.5) please do not insert text because i have not created a filter yet  <br> 
Created Date: <input type="text" name="created_date" value="<?= $api_data[0]->created_date  ?>"> example : 27072021 (dd/mm/yyyy) please do not insert text because i have not created a filter yet <br> 
<input type="hidden" name="id_product" value="<?= $api_data[0]->id_product  ?>" style="width:350px">
<input type="submit">
</form>