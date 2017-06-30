#echo Changing tracklet dimensions for $1 H=$2 W=$3 L=$4
sed -e 's/<h>[0-9\.]*/<h>'$2'/g' -e 's/<w>[0-9\.]*/<w>'$3'/g' -e 's/<l>[0-9\.]*/<l>'$4'/g' $1 > $5
