FROM alpine:latest
RUN apk add --no-cache bind bind-tools bash \
&& mkdir -p /var/log/named \
&& touch /var/log/named/named.log \
&& chmod -R 777 /var/log/named
RUN mkdir -p /etc/bind /var/cache/bind /var/lib/bind /var/log \
    && chown -R named:named /etc/bind /var/cache/bind /var/lib/bind /var/log
EXPOSE 53/udp 53/tcp
CMD ["named", "-g", "-u", "named", "-c", "/etc/bind/named.conf"]