#!/user/bin/env ash

MONGO_PORT="27017"

wait_ready() {
    echo "Waiting $1 at port $2"
    until nc -z $1 $2 ; do
        sleep 1
    done
}

wait_ready db $MONGO_PORT
exec python3 manage.py runserver 0.0.0.0:8000
