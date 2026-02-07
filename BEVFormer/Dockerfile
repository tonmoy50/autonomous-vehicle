FROM nvidia/cuda:11.1.1-cudnn8-devel-ubuntu18.04

ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /workspace

# --------------------
# System dependencies
# --------------------
RUN apt-get update && apt-get install -y \
    build-essential \
    ca-certificates \
    curl \
    git \
    wget \
    bzip2 \
    vim \
    gcc-7 g++-7 \
    libgl1 libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# --------------------
# Force GCC/G++ 7.3
# --------------------
RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-7 100 && \
    update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-7 100

ENV CC=gcc
ENV CXX=g++

# --------------------
# Install Miniconda (NO conda init)
# --------------------
ENV CONDA_DIR=/opt/conda
ENV PATH=$CONDA_DIR/bin:$PATH

RUN wget -q https://repo.anaconda.com/miniconda/Miniconda3-py38_23.3.1-0-Linux-x86_64.sh -O /tmp/miniconda.sh && \
    bash /tmp/miniconda.sh -b -p $CONDA_DIR && \
    rm /tmp/miniconda.sh && \
    conda clean -afy

# Make conda activation work automatically in bash
RUN echo ". $CONDA_DIR/etc/profile.d/conda.sh" >> /etc/bash.bashrc

# --------------------
# Sanity checks
# --------------------
RUN gcc --version && \
    g++ --version && \
    nvcc --version && \
    conda --version

CMD ["/bin/bash"]
