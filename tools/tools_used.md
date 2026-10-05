# Tools Used

## 1. MxToolbox

### Purpose

MxToolbox was used to inspect publicly available email and DNS
authentication information.

### SPF Check

SPF lookup was used to inspect the Sender Policy Framework record
of a domain.

SPF helps identify which servers are authorized to send email
on behalf of a domain.

### DMARC Check

DMARC lookup was used to inspect the domain's published DMARC
policy.

DMARC helps receiving mail systems determine how to handle
messages that fail authentication requirements.

### DKIM Check

DKIM lookup can be used to check whether a valid DKIM public key
is published for a domain when the DKIM selector is known.

### Additional Tools

MxToolbox also provides DNS, WHOIS, IP, blacklist and other
network diagnostic tools.

## Evidence

Screenshots of the SPF and DMARC lookups are stored in:

`screenshots/`