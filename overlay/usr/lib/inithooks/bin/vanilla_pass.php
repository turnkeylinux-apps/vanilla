<?php

define('APPLICATION', 'Vanilla');
define('PATH_LIBRARY', '/var/www/vanilla/library');

include PATH_LIBRARY . '/core/class.passwordhash.php';

if(count($argv)!=2) die("usage: $argv[0] password\n");

$password = $argv[1];

$PasswordHash = new Gdn_PasswordHash();
print $PasswordHash->HashPassword($password);

?>
