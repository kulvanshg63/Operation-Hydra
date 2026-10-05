# Operation Hydra
## Unraveling a Multi-Vector Cyber Crime Involving Phishing, Spoofing & Financial Fraud

**Subject:** Cyber Crime Investigation and Digital Forensics  
**Assignment:** Assignment 2 – Unit 2: Types of Cyber Crimes  
**Student:** Kulvansh Raghav  
**Case Type:** Simulated Cyber Crime Investigation  
**Date:** September 2026

---

# 1. Executive Summary

Operation Hydra is a simulated multi-stage cyber-crime investigation
designed to demonstrate how multiple cyber-crime techniques can be
connected within a single attack campaign.

The simulated attack begins with phishing emails designed to deceive
employees into clicking fraudulent links or opening a suspicious
attachment. The attack then progresses through spoofing, credential
theft, simulated unauthorized access, malware delivery and financial
fraud.

The investigation analyzes three simulated phishing emails, their
headers and authentication results. SPF, DKIM and DMARC concepts are
examined to demonstrate email authentication analysis. Simulated IP
addresses and domains are treated as Indicators of Compromise (IOCs).

A simulated Trojan named `Invoice_2026.exe` is analyzed as a malware
delivery mechanism. The investigation also reconstructs a simulated
financial transaction trail from the victim account to a mule account
and subsequently to a simulated cryptocurrency wallet.

The investigation concludes with legal, ethical and stakeholder-impact
analysis and provides recommendations for preventing similar attacks.

All evidence, domains, accounts, IP addresses, transactions and
malware indicators used for the Hydra case are simulated for
educational purposes.

---

# 2. Case Background

## 2.1 Organization

The simulated victim organization is:

**ApexTech Solutions Pvt. Ltd.**

The organization is targeted by a cyber-criminal campaign that uses
social engineering and technical deception to compromise employees.

## 2.2 Attack Objective

The simulated attacker attempts to:

1. Deceive employees through phishing emails.
2. Obtain credentials through a spoofed login page.
3. Gain unauthorized access using stolen credentials.
4. Deliver a simulated Trojan through an email attachment.
5. Obtain sensitive financial information.
6. Initiate a fraudulent financial transaction.
7. Transfer the funds through a simulated mule account.
8. Move a portion of the funds to a simulated cryptocurrency wallet.

## 2.3 Attack Chain

The simulated attack can be represented as:

Phishing Email
↓
Spoofed Website
↓
Credential Theft
↓
Simulated Unauthorized Access
↓
Malicious Attachment
↓
Simulated Trojan
↓
Financial Fraud
↓
Mule Account
↓
Simulated Cryptocurrency Wallet

---

# 3. Cybercrime Classification

The Hydra campaign contains multiple cyber-crime categories.

| Cyber Crime | Role in Operation Hydra |
|---|---|
| Phishing | Fraudulent emails are used to deceive victims |
| Spoofing | Fake domains and identities imitate trusted services |
| Credential Theft | Victim credentials are targeted |
| Unauthorized Access | Stolen credentials are used in the simulated scenario |
| Malware Delivery | A simulated Trojan is delivered as an attachment |
| Financial Fraud | A simulated fraudulent transaction is initiated |
| Spamming | Multiple fraudulent messages are distributed |

The combination of these activities demonstrates how a cyber-crime
campaign can involve several related offences rather than one isolated
incident.

---

# 4. Phishing and Spoofing Investigation

## 4.1 Email 01 – Password Expiry

The first simulated email claims to originate from IT Support.

The message creates urgency by informing the employee that their
password will expire and that the account may be suspended.

The email directs the user to:

`https://apextech-login-security.example/verify`

### Indicators

- Urgent language
- Account-suspension threat
- Suspicious sender domain
- Suspicious verification URL
- Simulated SPF failure
- Simulated absence of DKIM
- Simulated DMARC failure

The suspected objective is credential harvesting.

---

## 4.2 Email 02 – Fake Invoice

The second email claims to originate from the Finance Department.

The email contains:

`Invoice_2026.exe`

The use of an executable attachment is suspicious because the user is
instructed to execute the file to view an invoice.

### Indicators

- Suspicious finance-related domain
- Executable attachment
- Urgency
- Simulated SPF failure
- Simulated DKIM failure
- Simulated DMARC failure

The suspected objective is malware delivery through social engineering.

---

## 4.3 Email 03 – Payment Verification

The third email claims that a payment of INR 48,500 has been initiated.

The user is instructed to verify the transaction through:

`https://payment-verification.example/confirm`

### Indicators

- Financial fear/social engineering
- Suspicious payment-related domain
- Suspicious verification URL
- Simulated SPF failure
- Simulated absence of DKIM
- Simulated DMARC failure

The suspected objective is to obtain sensitive financial information.

---

# 5. Email Authentication Analysis

## 5.1 SPF

SPF stands for Sender Policy Framework.

SPF allows a domain to specify which servers are authorized to send
email on its behalf.

In the simulated Hydra headers, SPF results are represented as
`fail` for suspicious messages.

## 5.2 DKIM

DKIM stands for DomainKeys Identified Mail.

DKIM uses a digital signature associated with an email domain.
The receiving system can use the published public key to verify the
signature.

The simulated Hydra messages contain either no DKIM signature or a
failed DKIM result.

## 5.3 DMARC

DMARC stands for Domain-based Message Authentication, Reporting and
Conformance.

DMARC provides a policy framework for handling messages that do not
satisfy the domain's authentication requirements.

The simulated Hydra messages contain a DMARC failure.

## 5.4 Investigation Method

For real email investigations, an investigator can examine the raw
email headers and inspect the `Authentication-Results` header.

DNS lookup tools can also be used to examine published SPF and DMARC
records. DKIM can be investigated using the signing domain and selector
contained in a DKIM signature.

MxToolbox was used to demonstrate public DNS and email-authentication
lookup methodology.

---

# 6. IP and WHOIS Investigation

The simulated Email 03 contains:

`192.0.2.55`

This IP address is intentionally selected from a documentation/example
range.

It is therefore not treated as real attacker infrastructure.

In a real investigation, investigators could perform:

- WHOIS lookup
- DNS lookup
- Reverse DNS lookup
- IP reputation analysis
- Abuse database checks
- Mail-server log correlation

An IP address alone does not prove the identity of an attacker.

Additional evidence and correlation would be required.

---

# 7. Indicators of Compromise

The simulated investigation identified the following IOCs:

| IOC Type | Example |
|---|---|
| Domain | apextech-security.example |
| Domain | payment-secure.example |
| URL | payment-verification.example/confirm |
| IP | 192.0.2.55 |
| IP | 198.51.100.27 |
| Filename | Invoice_2026.exe |
| Hash | SIMULATED_SHA256_HASH |
| Account | VIRTUAL_MULE_M001 |
| Wallet | VIRTUAL_WALLET_W001 |

All IOCs in this case are simulated.

---

# 8. Malware Payload Analysis

## 8.1 Sample

**Filename:** `Invoice_2026.exe`

## 8.2 Classification

The simulated payload is classified as a **Trojan**.

A Trojan is malware that is presented as something legitimate or
useful in order to deceive the user into executing it.

In Operation Hydra, the file is presented as an invoice but is
represented as malicious software in the simulated scenario.

## 8.3 Attack Vector

The malware delivery chain is:

Phishing Email
↓
Fake Finance Message
↓
Invoice_2026.exe
↓
Victim Execution
↓
Simulated Trojan

## 8.4 Simulated Behavior

The simulated analysis records:

1. The file is received through a phishing email.
2. The user executes the file.
3. A dummy execution event is recorded.
4. A harmless analysis log is created.
5. No real credentials are accessed.
6. No real files are modified or deleted.
7. No external command-and-control connection is established.

## 8.5 Evidence

The malware evidence consists of:

- Filename
- Simulated hash
- Sender information
- Associated domain
- Execution log
- IOC record

No real malicious executable is included or executed.

---

# 9. Financial Fraud Investigation

## 9.1 Initial Transaction

The simulated victim transfers:

**INR 48,500**

to:

**Virtual Mule Account M001**

Transaction ID:

`TXN001`

## 9.2 Subsequent Transfers

M001 subsequently transfers:

**INR 45,000 → Virtual Wallet W001**

and:

**INR 2,500 → Virtual Account M002**

The simulated remaining balance is:

**INR 1,000**

## 9.3 Money Flow

Victim Account
↓
INR 48,500
↓
Virtual Mule M001
├── INR 45,000 → Virtual Wallet W001
└── INR 2,500 → Virtual Account M002

## 9.4 Investigation Finding

The transaction sequence demonstrates how investigators can follow
the movement of funds using transaction IDs, timestamps, source
accounts and destination accounts.

The cryptocurrency wallet used in this assignment is entirely
fictional and is included only to demonstrate the concept of financial
tracing.

---

# 10. Legal Analysis

## 10.1 Important Legal Note

The assignment refers to the Indian Penal Code (IPC). For the current
legal analysis, the Bharatiya Nyaya Sanhita, 2023 is considered because
it is the current criminal-law framework.

The precise legal provisions applicable to a real case would depend
on the evidence and circumstances established during investigation.

## 10.2 Unauthorized Access

The Information Technology Act, 2000 contains provisions dealing with
unauthorized access and related acts involving computer resources.

Section 43 addresses specified unauthorized acts involving computer
systems, while Section 66 addresses dishonest or fraudulent computer
related acts.

## 10.3 Identity Theft

Section 66C of the Information Technology Act addresses identity theft,
including dishonest or fraudulent use of another person's password or
other unique identification feature.

## 10.4 Cheating by Personation

Section 66D of the Information Technology Act addresses cheating by
personation using a computer resource or communication device.

This is relevant to the simulated phishing and impersonation stages.

## 10.5 Financial Fraud

Section 318 of the Bharatiya Nyaya Sanhita, 2023 deals with cheating.

The applicability of a particular provision to a real incident would
depend on the established facts and evidence.

## 10.6 International Frameworks

International cybercrime investigations may involve frameworks such as:

- Computer Fraud and Abuse Act (CFAA)
- Budapest Convention on Cybercrime
- GDPR where its requirements and territorial scope apply

These frameworks are useful for understanding international
cooperation, unauthorized access and protection of personal data.

---

# 11. Ethical Considerations

## 11.1 Privacy

Investigators may encounter personal information while examining
emails, systems and transaction records.

Only relevant information should be collected and handled securely.

## 11.2 Cryptocurrency Tracing

Blockchain transactions may be traceable, but a wallet address does
not automatically identify a real-world person.

Investigators should avoid making unsupported identity claims.

## 11.3 Honeypots

Honeypots may help investigators study attacker behavior, but their
use should remain within legal and ethical boundaries.

## 11.4 Evidence Integrity

Digital evidence must be preserved carefully.

Investigators should maintain records of:

- What was collected
- When it was collected
- How it was handled
- What analysis was performed

## 11.5 Authorization

Investigators must not access systems without appropriate
authorization.

The scope of investigation should be clearly defined.

---

# 12. Stakeholder Impact

## Victims

Potential impacts include:

- Financial loss
- Emotional stress
- Loss of privacy
- Loss of trust in digital services

## Organization

Potential impacts include:

- Financial recovery costs
- Reputational damage
- Operational disruption
- Incident-response costs

## Financial Institutions

Banks and payment providers may need to investigate suspicious
transactions and cooperate with authorized investigations.

## Society

Large-scale phishing campaigns can reduce public trust in digital
payments and online services.

---

# 13. Prevention and Recommendations

## For Individuals

1. Do not click unexpected links.
2. Verify suspicious messages independently.
3. Avoid opening unexpected executable attachments.
4. Use multi-factor authentication.
5. Enable transaction alerts.
6. Report suspected phishing.

## For Organizations

1. Deploy SPF, DKIM and DMARC.
2. Provide phishing-awareness training.
3. Use multi-factor authentication.
4. Monitor unusual login behavior.
5. Centralize security logs.
6. Establish incident-response procedures.
7. Restrict execution of unnecessary file types.

## For Financial Security

1. Monitor unusual transactions.
2. Implement fraud-detection systems.
3. Provide rapid reporting mechanisms.
4. Educate customers about payment phishing.

---

# 14. Investigation Limitations

This investigation is a simulated academic exercise.

The following artifacts are fictional or documentation-only:

- Domains
- IP addresses
- Email accounts
- Transaction accounts
- Cryptocurrency wallet
- Malware sample
- Malware hash
- Transaction records

Therefore, the results must not be interpreted as evidence of a
real-world criminal incident.

Real investigations would require legally obtained evidence,
validated logs, forensic acquisition, chain-of-custody procedures and
appropriate investigative authority.

---

# 15. Conclusion

Operation Hydra demonstrates how phishing, spoofing, credential theft,
malware delivery and financial fraud can be connected within one
multi-stage cyber-crime campaign.

The investigation used simulated email headers, authentication
results, IP information, IOC records, malware execution logs and
financial transaction records to reconstruct the attack.

The analysis demonstrates the importance of correlating different
types of digital evidence rather than examining each artifact in
isolation.

The investigation also demonstrates that cybersecurity requires both
technical controls and user awareness. Strong email authentication,
multi-factor authentication, transaction monitoring, security
training and effective incident response can reduce the likelihood
and impact of similar attacks.

---

# 16. References

1. Information Technology Act, 2000 – Government of India,
   India Code.

2. Bharatiya Nyaya Sanhita, 2023 – Government of India,
   India Code.

3. MxToolbox – DNS, SPF, DKIM, DMARC and WHOIS investigation tools.

4. Budapest Convention on Cybercrime – Council of Europe.

5. Computer Fraud and Abuse Act (CFAA) – United States legislation.

6. General Data Protection Regulation (GDPR) – European Union.

---

# 17. Authorship Declaration

I, **Kulvansh Raghav**, declare that this assignment was prepared
for academic purposes as a simulated cyber-crime investigation.

The investigation artifacts used in the Operation Hydra case are
fictional or documentation-only examples created for educational
analysis.

The work focuses on understanding cybercrime investigation,
digital evidence, phishing, spoofing, malware analysis, financial
fraud tracing, legal considerations and ethical responsibilities.