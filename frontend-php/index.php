<html>
<body>
<?php

//$api_key = 'sjadhuwhduiahhsjhduwudhjxxgq'; //this is admin (can do anything)

$api_key = 'shdyegdhzudifhesydahwyeygd'; //this is user (can not update,insert,and delete data)
$api_url = 'http://127.0.0.1:5000/product/'.$api_key;
 

// Read JSON file
$json_data = file_get_contents($api_url);

// Decode JSON data into PHP array
$response_data = json_decode($json_data);

// All user data exists in 'data' object
$api_data = $response_data->product;


// Traverse array and display user data


?>


<a href="tambah.php">add data</a><br><br>


<table border="1">
    <thead>
        <td>Product Name</td>
        <td>Product Type</td>
        <td>Price (dolar)</td>
        <td>Created Date</td>
        <td>Action 1</td>
        <td>Action 2</td>
    </thead>
    <tbody>
        
        <?php
        
        foreach ($api_data as $data) {
            echo "<tr>";
            echo "<td>".$data->name_product."</td>";
            echo "<td>".$data->type_product."</td>";
            echo "<td>".$data->price."</td>";
            echo "<td>".$data->created_date."</td>";    
            echo "<td><a href='update.php?id=$data->id_product'> EDIT </a></td>";
            echo "<td><a href='delete.php?id=$data->id_product'> DELETE </a></td>";
            echo "</tr>";
        }
        
        ?>
        
    </tbody>
</table>
    </body>
</html>