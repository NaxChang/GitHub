
FROM arm64v8/rockylinux:8.8
RUN dnf install -y findutils && dnf clean all
COPY check_dir /usr/local/bin/
RUN chmod +x /usr/local/bin/check_dir
ENTRYPOINT ["check_dir"]


