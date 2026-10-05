# Phishing Investigation

## Email 01 – Password Expiry

### Observations

The email claims to originate from the IT Support Team and informs the
recipient that their corporate password will expire.

The email asks the recipient to click a verification link.

### Suspicious Indicators

1. Urgent language is used.
2. The recipient is threatened with account suspension.
3. The sender uses a suspicious look-alike domain.
4. The verification URL uses a different suspicious domain.
5. SPF authentication fails.
6. DKIM authentication is absent.
7. DMARC authentication fails.
8. The apparent purpose of the email is to obtain user credentials.

### Preliminary Classification

The email is classified as a simulated phishing attempt.

### Suspected Objective

Credential harvesting through a fraudulent login/verification page.


---

## Email 02 – Fake Invoice

### Observations

The second email claims to originate from the Finance Department.

It contains an executable attachment named `Invoice_2026.exe`.

### Suspicious Indicators

1. The sender uses a suspicious finance-related domain.
2. SPF authentication fails.
3. DKIM authentication fails.
4. DMARC authentication fails.
5. The message creates urgency around an invoice.
6. The attachment uses the `.exe` executable file extension.
7. The recipient is instructed to execute the attachment.

### Preliminary Classification

The email is classified as a simulated phishing email
used as a malware delivery vector.

### Suspected Objective

The suspected objective is to convince the victim to execute
a malicious-looking attachment.


---

## Email 03 – Payment Verification

### Observations

The third email claims that a payment of INR 48,500 has been
initiated and asks the recipient to verify the transaction.

### Suspicious Indicators

1. The email creates fear about an unauthorized transaction.
2. The sender uses a suspicious payment-related domain.
3. SPF authentication fails.
4. DKIM authentication is absent.
5. DMARC authentication fails.
6. The email directs the victim to a verification URL.
7. The message attempts to obtain a response from the victim
   through social engineering.

### Preliminary Classification

The email is classified as a simulated phishing attempt
associated with financial fraud.

### Suspected Objective

The suspected objective is to redirect the victim to a fraudulent
verification page and obtain sensitive financial information.