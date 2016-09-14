vcl 4.0;

# Default backend definition. Set this to point to your content server.
backend default {
    .host = "127.0.0.1";
    .port = "8000";
}


sub vcl_recv {
    if (req.url ~ "^/admin" || req.http.cookie ~ "sessionid" ){
        return (pass);
    } else {
        unset req.http.Cookie;
    }
    return (hash);
}

sub vcl_hit {
   if (obj.ttl >= 0s) {
       // A pure hit, deliver it
       return (deliver);
   }
   if (obj.ttl + obj.grace > 0s) {
       // Object is in grace, deliver it
       // Automatically triggers a background fetch
       return (deliver);
   }
   // fetch & deliver once we get the result
   return (fetch);
}

# Happens after reading the backend response headers
sub vcl_backend_response {
  set beresp.grace = 5m;
  set beresp.ttl = 5s;
  return (deliver);
}
