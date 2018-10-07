<html>
	<head>
		<meta name="viewport" content="user-scalable=no, width=device-width, initial-scale=1, maximum-scale=1">          

		<!-- jQuery -->
		<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.1/jquery.min.js" type="text/javascript"></script>

		<!-- nanogallery2 -->
		<link  href="https://unpkg.com/nanogallery2@2.1.0/dist/css/nanogallery2.min.css" rel="stylesheet" type="text/css">
		<script  type="text/javascript" src="https://unpkg.com/nanogallery2@2.1.0/dist/jquery.nanogallery2.min.js"></script>
	</head>
	<body>
		<?php	
			echo '
			<form method="get">
				Date: 
				<select name="date">';
					 
			# Get all directories
			$directories = array();
			$ds = glob('detection/' . "*");
			foreach($ds as $d){
				if(is_dir($d)){		
						
					$final = str_replace('detection/',"",$d);
					echo '<option value="'.$final.'" >'.$final.'</option>';
				}
			}		
			echo '
				</select>
				<input type="submit" name="submit"/>
			</form>';
	
		
		$fs = array();
		if(isset($_GET['date']) && !empty($_GET['date'])){	
			
			$files = glob('detection/'.$_GET['date'].'/*');
			foreach($files as $file){			
				$final = str_replace('detection/', "", $file);
				array_push($fs, $final);
			}		
		}
		?>

		<div id="nanogallery2" data-nanogallery2='{ "thumbnailHeight": 150, "thumbnailWidth": 150, "itemsBaseURL": "/detection/"}' >
		<?php
			foreach($fs as $file){
				$n = str_replace('.png', "", $file);
				$name = explode("/", $n);
				echo '<a href="'.$file.'" data-ngThumb="'.$file.'" >'.$name[1].'</a>';
			}
		?>
		</div>
	</body>
</html>