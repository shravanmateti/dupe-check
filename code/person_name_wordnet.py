#Extract person name using Wordnet

import nltk
from nameparser.parser import HumanName
from nltk.corpus import wordnet


person_list = []
person_names=person_list
def get_human_names(text):
    tokens = nltk.tokenize.word_tokenize(text)
    pos = nltk.pos_tag(tokens)
    sentt = nltk.ne_chunk(pos, binary = False)

    person = []
    name = ""
    for subtree in sentt.subtrees(filter=lambda t: t.label() == 'PERSON'):
        for leaf in subtree.leaves():
            person.append(leaf[0])
        if len(person) > 1: #avoid grabbing lone surnames
            for part in person:
                name += part + ' '
            if name[:-1] not in person_list:
                person_list.append(name[:-1])
            name = ''
        person = []
#     print (person_list)

text = """
Clarence Goh
Date of Birth: 12 April 1984
Gender: Male
Citizenship: Singaporean
Mobile Number: 92311889	
Email: rencegoh@gmail.com
Postal Address: 365D Upper Serangoon Road Singapore 537365


Education
________________________________________

Accountancy & Financial Management 
University of Portsmouth
June 2017 to Present

GCE A Levels, LCCI Level 2 Book-Keeping & Accounts
Millenia Institute
Jan 2002 to Dec 2004

GCE O Levels
Ghim Moh Secondary School
Jan 1997 to Dec 2001


Technical Skills
________________________________________

	Microsoft Office: Word, Excel, Power point
	SAP 


Date of Availability
________________________________________

	Two Months Notice









Work Experience
________________________________________

Dec 2014 to Present 
Rockworth Capital Partners Pte Ltd
Fund Accountant (Permanent)

	Work with external fund accountants and property accountants to ensure that financial
     reports for the trust entities are prepared on time with transactions recorded with appropriate
     accounting treatment.
	Manage the trust entities’ bank accounts, including preparation of trustee instruction,
      ensuring sufficient balance, processing payment of invoices in accordance with agreed upon
      amount, tracking interest expense and remittances from investment properties.
	Prepare journals for respective trust entities.
	Review completeness of financial accounts prepared by external vendors, review variance
     analysis of property manager’s financial accounts and review bank reconciliations.
	Prepare rent straight lining for respective trusts entities on their tenant’s lease period.
	Review financial statements of respective trusts entities during their financial year end.
	Prepare Australia Business Activity Statements and IRAS GST claims for respective trusts.
	Co-ordinate with auditors to provide schedules and relevant supporting.
	Co-ordinate with bank, investor, solicitors and trustee on funding requirements required for
     the settlement of new property acquisitions to ensure funds are provided on time to effect
     sale completion.
	Manage the trust entities’ bank accounts, including preparation of trustee instruction,
      ensuring sufficient balance, processing payment of invoices in accordance with agreed upon
      amount, tracking interest expense and remittances from investment properties.

Jan 2013 to Dec 2014
Prudential Assurance Company Singapore Pte Ltd 
Finance Associate (Permanent)

	Prepare Portfolio Bond funds subscription & redemption order process & fund transfer.
	Reconcile Portfolio Bond Funds & fund houses unit holdings.
	Handle FOF, EIP unit deal, Prulife surrenders & claims.
	Reconcile FOF, EIP units in EIP system & UOBAM holdings. 
	Prepare Interfund (normal) book settlement & payment.
	Prepare NAV price variance reasonableness check & upload of PruLink, Portfolio Bonds & EIP daily unit prices.
	Prepare cheques, cashier orders & direct credit payments.
	Process stop payments on cheques & cashier orders. 
	Posting of journals.
	Review of finance payment listings that are not approved & authorized.
	Review of payment reversal listing.
	Update premium & commission for embedded component & outstanding provisions.
	Prepare monthly bank reconciliation.
	Perform ad-hoc duties when required and general administrative work.



Jul 2012 to Jan 2013
Chevron Phillips Chemicals Asia Pte Ltd 
Accounts Assistant (Permanent)

	Process supplier invoices for payment on a timely basis. Verify items on invoice
to purchase orders, checking of prices and ensure all documents are in order.
	Reviews GRIR account and reconciles creditors statement of accounts with the payable
ledger, liaising with suppliers on their account status.
	Assists in monitoring and tracking of capital expenditure against budgets and updating of 
monthly capex reports for CPSC and CPCM. 
	Classifies records and accrues billed and unbilled liabilities.
	Ensure that the monthly CPIC commission income, expenses received, paid are correct and in accordance with the sales agency agreements.
	Perform quarterly reconciliation of CPSC and CPCM accounts.
	Assists in the monthly remeasurement and translation process and analyze the exchange gain and loss for CPSC and CPCM.
	Posts transactions to the general, special and subsidiary ledgers on a timely basis.
	Reviews and analyses monthly reasonablesness of CPSC and CPCM accounts.
	Apportions and charges out expenses to cost centres or intercompany according to approved bases.
	Analyses and reconciles the general ledger accounts to the subsidiary ledgers on monthly basis.
	Assist in managing the books of CPCM.
	Process CPCM and CPCAU employee’s travel expense statements on a timely and accurate basis.
	Performs quarterly and annual physical inventory count of raw materials, spare parts and finished goods.
	Perform ad-hoc duties when required and general administrative work.

Dec 2011 to Jan 2012
Furniture Origins Pte Ltd
Accounts Assistant (Temporary)

	Verify and provide tax expenses details using MS Navision.
	Prepared invoices for factoring of accounts receivables.
	Examined and prepare accounts schedules for audit purposes.
	Verify the validity of supporting documents and prepare debit notes for intercompany cross charges.
	Verify and update VAT figures in Payables listing.
	Performed ad-hoc duties when required and general administrative work.


Jul 2011 to Aug 2011
Grey Group Pte Ltd
Accounts Assistant (Temporary)

	Assisted in General Ledger, Accounts Payables and Receivables with Adeptman SAP.
	Prepared invoices and payments for Accounts Payables section.
	Revalued Accounts Payables and Receivables, and update month end closing schedule.
	Maintained Fixed Assets Register.
	Performed ad-hoc duties when required and general administrative work.

Jan 2010 to Apr 2010
Ministry of Education
Administrative Assistant (Contract)

	Reclassified funds into application category for verification.
	Prepared documents and emails to send to school.
	Performed data entry for budgeting exercise and general administrative work.
	Called HODs of schools to verify their ICT plans.
	Verified the accuracy and validity of schools ICT funding request.
	Reclassified of ICT plan into various technology types.

Nov 2009 to Dec 2009
Incall System Private Limited
Call Centre Agent (Temporary)

	Answered inbound and outbound calls.
	Provided call backs and taking messages at quick response time to assist clients enquiries.
	Verified client’s particulars with client database in CRM software to ensure there’s no misstatement.
	Performed data entry on client’s particulars and match them to available job fairs.

Jun 2008 to Aug 2008
Ministry of Education
Administrative Assistant (Temporary)

	Created surveys and interviews for teachers and students in primary schools to gather
	feedback on ICT programmes.
	Used video to capture and observe students behaviour during ICT classes.
	Attended meetings, prepared presentations and reviewed on students responses towards ICT lessons.
	Transcribed interviews from audio and video recordings into documents and general administrative work.

Apr 2007 to Jul 2007
NIKE By B.I.R.D
Retail Assistant (Temporary)

	Provided assistance to customers in locating merchandise and utilised special product
knowledge to advice customers queries on the selection of merchandises.
	Ensuring the smooth running of a store as a valued team member, maintaining and
arranging merchandises.
	Achieved set sales targets in various months.
	Helped train and develop new sales assistants.
	Used of POS system to process payments of various kinds.





Jan 2007 to Mar 2007
Bods and Bodynits
Retail Assistant (Temporary)

	Provided assistance to customers in locating merchandise and answering a variety of
questions concerning general merchandises.
	Meeting of individual sales target in various months.
	Stocking, replenishing and keeping of merchandises in an orderly and neat appearance.
	Processed payments of various kinds.
"
"""

names = get_human_names(text)
for person in person_list:
    person_split = person.split(" ")
    for name in person_split:
        if wordnet.synsets(name):
            if(name in person):
                person_names.remove(person)
                break
print(person_names)