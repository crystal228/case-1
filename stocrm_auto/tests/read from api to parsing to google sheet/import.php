<?php

require __DIR__ . '/vendor/autoload.php';

$credentialsPath = 'D:/Work/php/xampp/htdocs/fortestblad/credentials.json';
$spreadsheetId = '1rSaegikZgR5hZQMN4J9gM4Id--VflZYcFJgCb-E2WVg';
$range = 'Sheet1!A1';
$apiUrl = "https://dev.dev.stocrm.ru/wh/sandbox/datagen.php";

function getProductsFromApi($apiUrl) {
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $apiUrl);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    $response = curl_exec($ch);
    curl_close($ch);

    return json_decode($response, true);
}

function appendDataToGoogleSheet($spreadsheetId, $range, $values, $credentialsPath) {
    $client = new \Google_Client();
    $client->setAuthConfig($credentialsPath);
    $client->addScope(\Google_Service_Sheets::SPREADSHEETS);

    $service = new \Google_Service_Sheets($client);

    $body = new \Google_Service_Sheets_ValueRange([
        'values' => $values
    ]);
    $params = [
        'valueInputOption' => 'RAW',
        'insertDataOption' => 'INSERT_ROWS'
    ];

    $result = $service->spreadsheets_values->append($spreadsheetId, $range, $body, $params);
    return $result;
}

$products = getProductsFromApi($apiUrl);

$values = [];
foreach ($products as $product) {
    $values[] = [$product['name'], $product['price'], $product['discount']];
}

appendDataToGoogleSheet($spreadsheetId, $range, $values, $credentialsPath);

echo "Data imported successfully.";
?>
