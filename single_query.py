#!/usr/bin/env python
import time
import bugzilla

URL = "bugzilla.redhat.com"
bzapi = bugzilla.Bugzilla(URL)

query = bzapi.build_query(
    product="OpenShift Container Platform",
    component="Networking",
    sub_component="ovn-kubernetes")

query["status"] = "NEW"

t1 = time.time()
bugs = bzapi.query(query)
t2 = time.time()
print("Found %d bugs with our query" % len(bugs))
print("Query processing time: %s" % (t2 - t1))

for bug in bugs:
    print("Fetched bug #%s:" % bug.id)
    print("  Product   = %s" % bug.product)
    print("  Assigned  = %s" % bug.assigned_to)
    print("  Component = %s" % bug.component)
    print("  Status    = %s" % bug.status)
    print("  Resolution= %s" % bug.resolution)
    print("  Summary   = %s" % bug.summary)
    print("-------------------\n")
