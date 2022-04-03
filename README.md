# Quick documentation
- [First Steps](#first-steps)
  * [Setting env](#setting-env)
  * [Bashing](#bashing)
  * [Querying](#querying)

This is quick notes page as reference for useing `bugzilla-cli` command line.  
**bugzilla-cli** project is available at: https://github.com/python-bugzilla/python-bugzilla

## First Steps
First, go to https://bugzilla.redhat.com and click: **Username -> Preferences -> API Keys**.  

**ATENTION:**  
As soon you click: "**Generate the API-key**" a long string will be generated with chars and numbers, COPY as it's only displayed **ONCE**.

```
$ mkdir -p ~/.config/python-bugzilla/ && cd ~/.config/python-bugzilla/ 
$ cat bugzillarc
[bugzilla.redhat.com]
api_key=pMqSdofimCiHqqq11113rr           <----- Long string generated once in the step above.
```

## Setting env
```
$ git clone https://github.com/python-bugzilla/python-bugzilla cd python-bugzilla
Cloning into 'python-bugzilla'...
remote: Enumerating objects: 6308, done.
remote: Counting objects: 100% (246/246), done.
remote: Compressing objects: 100% (166/166), done.
remote: Total 6308 (delta 144), reused 148 (delta 75), pack-reused 6062
Receiving objects: 100% (6308/6308), 1.40 MiB | 3.81 MiB/s, done.
Resolving deltas: 100% (4285/4285), done.
```

## Bashing
```
$ cd python-bugzilla
$ cat ./netquery
#!/bin/bash

developers=("foobar@email.com" \
        "devnull@email.com" \
        "supercar@email.com")
        
bz_status="NEW"

for dev in ${developers[@]}; do
    bz_number=$(./bugzilla-cli \
        query \
        --product "OpenShift Container Platform" \
        --component Networking \
        --sub-component ovn-kubernetes \
        --status "${bz_status}" | grep -i "${dev}" | wc -l)
    echo "The developer "${dev}" has ${bz_number} assigned as ${bz_status}"
done
```

Output Example:
```
python-bugzilla> ./netquery
The developer foobar@email.com has 1 assigned  
The developer devnull@email.com has 2 assigned  
The developer supercar@email.com has 2 assigned  
```

## Querying
Querying bugs for ovn-kubernetes in **NEW status**
```
./bugzilla-cli query --product "OpenShift Container Platform"  --component Networking --sub-component ovn-kubernetes --status NEW
#1894268 NEW        - pliu@redhat.com - SDN to OVN migration problem due to overlap with "Join network"
#1967779 NEW        - mcambria@redhat.com - Overlay node networking stops working
#1981277 NEW        - jtanenba@redhat.com - Found lots of 'dial tcp 10.x.x.x:xxx' with 'i/o timeout' or 'connection refused' errors when debugging "You must be logged in to the server (Unauthorized)" and "server is currently unable to handle the request"
#1988264 NEW        - fpaoline@redhat.com - In k8s 1.21 bump some sig-network tests are disabled due to being permanently broken on e2e-metal-ipi-ovn-ipv6
#1995706 NEW        - jluhrsen@redhat.com - ovnkube-config configmap specifies gateway mode as local, even when in reallity it is running in shared mode
#1999632 NEW        - cstabler@redhat.com - OpenShift 4.8.2 Cluster Install fails with node-primary-ifaddr annotation not found
#2002868 NEW        - dcbw@redhat.com - Node exporter not able to scrape OVS metrics
#2003228 NEW        - trozet@redhat.com - "Unidling should work with TCP" tests are flaky under ovn-kubernetes
#2028159 NEW        - jcaamano@redhat.com - OVN migration to 2nd interface on IPv6 with bond fails
#2047416 NEW        - ffernand@redhat.com - [4.9z] A pod cannot reach kubernetes.default.svc.cluster.local cluster IP
#2051995 NEW        - obraunsh@redhat.com - Duplicate BFD's causing ErrorAddingLogicalPort
#2053716 NEW        - cstabler@redhat.com - nbdb on 4.9.9 won't start
#2054391 NEW        - rravaiol@redhat.com - During cluster installation on Azure, worker machines are not applied with latest worker machineconfig.
#2055857 NEW        - obraunsh@redhat.com - SNO could not recover from a DHCP outage due to error 'failed to configure pod interface: timed out waiting for OVS port binding (ovn-installed)'
#2056050 NEW        - ffernand@redhat.com - [OVN]After reboot egress node,  lr-policy-list was not correct, some duplicate records or missed internal IPs
#2057951 NEW        - jcaamano@redhat.com - [scale][upgrade]dns co fail after upgrade,  dns-default pod Readiness probe failed
#2058912 NEW        - jtanenba@redhat.com - e2e-aws-ovn-windows job fails on a mco e2e test
#2059550 NEW        - bpickard@redhat.com - "Services should have session affinity timeout work" e2e tests are failing under ovn-kubernetes
#2059706 NEW        - ffernand@redhat.com - [OVN]After reboot egress node,  lr-policy-list was not correct, some duplicate records or missed internal IPs
#2060543 NEW        - astoycos@redhat.com - NodePort externalTrafficPolicy does not work for ovn-kubernetes
```
