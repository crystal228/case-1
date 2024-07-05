<?php

require __DIR__ . '/vendor/autoload.php';

$credentialsPath = 'D:/Work/php/xampp/htdocs/fortestblad/credentials.json';
$spreadsheetId = '1rSaegikZgR5hZQMN4J9gM4Id--VflZYcFJgCb-E2WVg';
$range = 'Sheet1!A1:Z1000'; 

function getDataFromGoogleSheet($spreadsheetId, $range, $credentialsPath) {
    $client = new \Google_Client();
    $client->setAuthConfig($credentialsPath);
    $client->addScope(\Google_Service_Sheets::SPREADSHEETS);

    $service = new \Google_Service_Sheets($client);
    $response = $service->spreadsheets_values->get($spreadsheetId, $range);

    return $response->getValues();
}

function updateGoogleSheet($spreadsheetId, $range, $values, $credentialsPath) {
    $client = new \Google_Client();
    $client->setAuthConfig($credentialsPath);
    $client->addScope(\Google_Service_Sheets::SPREADSHEETS);

    $service = new \Google_Service_Sheets($client);

    $body = new \Google_Service_Sheets_ValueRange([
        'values' => $values
    ]);
    $params = [
        'valueInputOption' => 'RAW'
    ];

    $result = $service->spreadsheets_values->update($spreadsheetId, $range, $body, $params);
    return $result;
}

$data = getDataFromGoogleSheet($spreadsheetId, $range, $credentialsPath);
$rowsToUpdate = [];
$updateRange = [];

foreach ($data as $index => $row) {
    if (isset($row[3]) && $row[3] == 'Y') { 
        $rowsToUpdate[] = $row;
        $data[$index][3] = ''; 
    }
}

if (!empty($rowsToUpdate)) {
    echo "Data to be sent to another API:\n";
    print_r($rowsToUpdate);

    updateGoogleSheet($spreadsheetId, $range, $data, $credentialsPath);
} else {
    echo "No data to update.";
}
?>
