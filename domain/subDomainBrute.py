from ESD import EnumSubDomain
from .models import Domain, SubDomain

def subDomainBrute(domain):
    dm = Domain()
    dm.dName = domain
    dm.save()
    domains = EnumSubDomain(domain=domain).run()
    sdm = SubDomain()
    for key,value in domains.items():
        sdm.dName = domain
        sdm.sdName = key
        sdm.ip = value
        sdm.save()

    print(domains)

if __name__ == '__main__':
    subDomainBrute('kingnet.com')