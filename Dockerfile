FROM odoo:16.0

USER root

RUN apt update
RUN apt install procps -y
RUN pip3 install ipdb
RUN pip3 install simplejson
RUN pip3 install pypeg2
