<?php require_once("config.php"); ?>
<!DOCTYPE html>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1" />

<?php 

$status = $_POST['want'];

switch ($status) {
	case 'login':
		require_once("login.php");
		break;
	case 'sign_up':
		require_once("sign_up.php");
		break;
	case 'feed':
		require_once("feed.php");
		break;
	default:
		require_once("error.php");
		break;
}

?>