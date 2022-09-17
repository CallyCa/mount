{
	"targets": [
		{
			"target_name": "src/gcc/mount",
			"sources": [ "src/gcc/mount.cc" ],
			"include_dirs": [ 
       			"<!(node -e \"require('nan')\")" 
          	]
		}
	]
}
