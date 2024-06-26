# Start with Debian
FROM debian:bullseye-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    ca-certificates \
    apt-transport-https \
    lsb-release \
    gnupg2 \
    tree \ 
    jq

# Install Docker CLI
RUN curl -fsSLk https://download.docker.com/linux/debian/gpg | apt-key add - \
    && echo "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list \
    && apt-get update \
    && apt-get install -y docker-ce-cli

# Install Docker Compose
RUN curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose \
    && chmod +x /usr/local/bin/docker-compose

# Install Python 3.9
RUN apt-get install -y python3.9

# Install Node.js and npm using NodeSource setup
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash - \
    && apt-get install -y nodejs python3-pip

RUN pip install pre-commit uvicorn fastapi pymongo pytest pandas pytest-cov python-dotenv pytest-mock-resources pytest-mock-resources[mongo] pylint black
RUN apt-get update && apt-get install -y git

RUN wget -O- https://apt.releases.hashicorp.com/gpg | gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg && \
    echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | tee /etc/apt/sources.list.d/hashicorp.list && \
    apt update && apt install terraform

RUN apt-get -y update && apt-get -y install locales 

# ENV LANG en_US.UTF-8
ENV LC_ALL C.UTF-8
ENV ANSIBLE_HOST_KEY_CHECKING=False
RUN pip install ansible
# Set the working directory
WORKDIR /workspace

ARG USERNAME
ARG USER_UID
ARG USER_GID


# Create the user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    #
    # [Optional] Add sudo support. Omit if you don't need to install software after connecting.
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

USER $USERNAME
# Clean up
RUN sudo apt-get clean && sudo rm -rf /var/lib/apt/lists/*
CMD ["/bin/bash"]
