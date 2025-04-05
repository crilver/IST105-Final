<?php
    $selected_items = $_GET['items'];  // A string like "0,1"
    
    $safe_items = array_map('escapeshellarg', $selected_items);
    $args = implode(' ', $safe_items);
    
    $command = escapeshellcmd("python3 party_planner.py $args");
    $output = shell_exec($command);

    echo $output;
?>
