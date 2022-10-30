#!/bin/sh
cd ur_node/

exec celery -A ur_node worker --loglevel=info --without-gossip --without-mingle --without-heartbeat -Ofair --pool=solo
