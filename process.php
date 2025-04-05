<?php
    $selected_items = $_GET['items'];  // A string like "0,1"
    
    $items = escapeshellarg($selected_items);
    
    $command = escapeshellcmd("python3 party_planner.py $items");
    $output = shell_exec($command);

    echo $output;
?>
