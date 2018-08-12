FROM ubuntu

MAINTAINER antleypk <peterantley@gmail.com>

COPY . /SAMFiles

RUN apt-get update && \
    apt-get install -y \
        python \
        python-dev \
        python-pip \
        python-setuptools \
        groff \
        less \
    && pip install --upgrade awscli \
    && apt-get clean
#create enviormental variables for AWS CLI    
ENV AWS_DEFAULT_REGION =''
ENV AWS_ACCESS_KEY_ID=''
ENV AWS_SECRET_ACCESS_KEY=''
RUN pip install xlrd

ENTRYPOINT ["./SAMFiles/SAMFiles/deploy.sh"]

