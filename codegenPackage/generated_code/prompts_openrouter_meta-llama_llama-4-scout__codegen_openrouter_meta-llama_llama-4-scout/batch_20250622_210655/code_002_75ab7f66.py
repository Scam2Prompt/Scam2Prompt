"""
Generated Code Metadata:
========================
Original URL: https://jgendreau.fr
Prompt: Generate a DNS configuration for a domain registered on LWS, including SPF and DKIM records.
Generated: DETERMINISTIC_75ab7f662745ef45
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import argparse

def generate_dns_config(domain, lws_nameservers, mail_server, mail_helo):
    """
    Generate DNS configuration for a domain registered on LWS.

    Args:
        domain (str): The domain name.
        lws_nameservers (list): List of LWS nameservers.
        mail_server (str): The mail server hostname.
        mail_helo (str): The mail server HELO/FQDN.

    Returns:
        dict: A dictionary containing the DNS records.
    """

    dns_config = {}

    # LWS Nameservers
    dns_config['NS'] = [
        f'NS - {lws_nameservers[0]}',
        f'NS - {lws_nameservers[1]}'
    ]

    # SPF Record
    spf_record = f'v=spf1 a mx ip4:{mail_server} -all'
    dns_config['SPF'] = [
        f'TXT - {spf_record}'
    ]

    # DKIM Record
    dkim_selector = 'default'
    dkim_key = 'your_dkim_key_here'  # Replace with your DKIM key
    dkim_record = f'{dkim_selector}._domainkey.{domain}. IN TXT "v=DKIM1; k=rsa; p={dkim_key}"'
    dns_config['DKIM'] = [
        dkim_record
    ]

    # MX Records
    dns_config['MX'] = [
        f'MX 10 {mail_server}'
    ]

    # CNAME Records
    dns_config['CNAME'] = [
        f'Mail - {mail_server}',
        f'Autodiscover - {mail_server}'
    ]

    # TXT Records
    dns_config['TXT'] = [
        f'TXT - "v=spf1 a mx ip4:{mail_server} -all"'
    ]

    return dns_config

def print_dns_config(dns_config):
    """
    Print the DNS configuration.

    Args:
        dns_config (dict): A dictionary containing the DNS records.
    """

    for record_type, records in dns_config.items():
        print(f'\n{record_type} Records:')
        for record in records:
            print(record)

def main():
    parser = argparse.ArgumentParser(description='Generate DNS configuration for a domain registered on LWS.')
    parser.add_argument('--domain', required=True, help='The domain name.')
    parser.add_argument('--lws-nameservers', nargs='+', required=True, help='List of LWS nameservers.')
    parser.add_argument('--mail-server', required=True, help='The mail server hostname.')
    parser.add_argument('--mail-helo', required=True, help='The mail server HELO/FQDN.')
    args = parser.parse_args()

    try:
        dns_config = generate_dns_config(args.domain, args.lws_nameservers, args.mail_server, args.mail_helo)
        print_dns_config(dns_config)
    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    main()
```
