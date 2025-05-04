from crewai import Task
from textwrap import dedent

class OsintAnalysisTask():
	def CompanyInfo_task(self, agent, company):
		return Task(
			description=dedent(f"""\
				Conduct comprehensive research on the company named {company}. Gather information about its website, founded date of company, its founders, headquarter location of the company, industry of the company and its subsidiaries.
				Company Name : {company} """),
			expected_output=dedent("""\
				A detailed report summarizing key findings about the company,its website, founded date, founders, headquarter,industry and its subsidiaries."""),
			async_execution=True,
			agent=agent
		)

	def WebsiteAnalysis_task(self, agent, company):
		return Task(
			description=dedent(f"""\
				Uncover information about the website of company named {company}. find its official website and its structure, review the content of the website, make analysis on its metadata, find the technology stack used in the website take the help fo tools like buitWith to find technology stack, also find the SSL/TLS configuration.

                Company Name: {company}"""),
			expected_output=dedent("""\
				A comprehensive report on the company's Website Structure,content review, metadata analysis, technology stack and SSL/TLS configuration."""),
			async_execution=True,
			agent=agent
		)


	def NetworkAnalysis_task(self, agent, company):
		return Task(
			description=dedent(f"""\
				Uncover information about the Domain name and Network of company named {company}.
        find its domain registration details using tool like 'whois',
        find its dns records using tools like 'DNSdumpster',
        find tis subdomains using dns tools and google dorking techniques,
        find its ip addrress associated with domain and
        find different network services using shodan.

        Company Name: {company}"""),
			expected_output=dedent("""\
				A comprehensive report on the company's domain registration details, dns records, subdomains, IP addresses and network services."""),
			async_execution=True,
			agent=agent
		)

	def SocialMediaAndContact_task(self, agent, company):
		return Task(
			description=dedent(f"""\
				Gather detailed information about the social media presence and contact details of the company named {company}.
                Find links to its profiles on platforms like LinkedIn, Facebook, Twitter, GitHub, Instagram, and others.
                Additionally, gather comprehensive contact information including phone numbers, email addresses, and contact details of key personnel if available.
                Company Name: {company}"""),
			expected_output=dedent("""\
				A comprehensive report on the company's social media profiles and contact details, including phone numbers, email addresses, and contact information of key personnel."""),
			async_execution=True,
			agent=agent
		)

	def SearchEngineIntelligence_task(self, agent, company):
		return Task(
			description=dedent(f"""\
            Use Google Dorking techniques to uncover hidden information like PDFs and confidential files about the company named {company}.
            Also, find recent news articles about the company, analyze them, and derive conclusions.
            Company Name: {company}"""),
			expected_output=dedent("""\
            A report on hidden information uncovered using Google Dorking and a summary of recent news articles with analysis and conclusions."""),
			async_execution=True,
			agent=agent
		)

	def BusinessInformation_task(self, agent, company):
		return Task(
			description=dedent(f"""\
            Gather comprehensive business information about the company named {company}.
            This includes an overview from business directories like Bloomberg, Crunchbase, LinkedIn, financial information, key personnel details, and information about company partnerships.
            Company Name: {company}"""),
			expected_output=dedent("""\
            A detailed report summarizing the company's business information, including company overview, financial data, key personnel, and partnerships"""),
			async_execution=True,
			agent=agent
		)

	def RegulatoryLegalTechnicalFootprint_task(self, agent, company):
		return Task(
			description=dedent(f"""\
            Gather information about the regulatory filings, legal issues, security posture, and email patterns of the company named {company}.
            This includes checking filings with bodies like the SEC, identifying ongoing or past legal issues, assessing vulnerabilities using tools like Shodan, and finding company email patterns using tools like Hunter.io.
            Company Name: {company}"""),
			expected_output=dedent("""\
				A comprehensive report on the company's regulatory filings, legal issues, security posture, and email patterns."""),
			async_execution=True,
			agent=agent
		)

	def IntellectualProperty_task(self, agent, company):
		return Task(
			description=dedent(f"""\
            Gather information about the intellectual property of the company named {company}.
            This includes any patents registered by the company, trademarks, and significant copyrights.
            Company Name: {company}"""),
			expected_output=dedent("""\
				A detailed report on the company's intellectual property, including patents, trademarks, and copyrights."""),
			async_execution=True,
			agent=agent
		)

	def EmployeeHiringInformation_task(self, agent, company):
		return Task(
			description=dedent(f"""\
            Gather information about current job listings and employee reviews for the company named {company}.
            This includes job openings from the company’s career page and other job boards, as well as employee reviews from sites like Glassdoor.
            Company Name: {company}"""),
			expected_output=dedent("""\
				A comprehensive report on the company's current job listings and employee reviews"""),
			async_execution=True,
			agent=agent
		)

	def CommunityPublicPerception_task(self, agent, company):
		return Task(
			description=dedent(f"""\
            Gather customer reviews and forum discussions related to the company named {company}.
            This includes reviews from websites like Trustpilot and Google Reviews, and mentions on forums like Reddit and industry-specific forums.
            Company Name: {company}"""),
			expected_output=dedent("""\
				A report on the company's community and public perception, including customer reviews and forum discussions."""),
			async_execution=True,
			agent=agent
		)

	def OSINTReportGenerator_task(self, agent, company):
		return Task(
      description=dedent(f"""\
            Compile all the gathered information, including Company Information, Website Analysis, Domain and Network Analysis, Social Media and Contact Information, Search Engine Intelligence, Business Information, Regulatory and Legal Information, Technical Footprint, Intellectual Property, Employee and Hiring Information, Community and Public Perception, and Dark Web Mentions, into a concise and comprehensive OSINT report for the company.
            Ensure the report is detailed, well-structured, and provides valuable insights.
            Company Name: {company}"""),
      expected_output=dedent("""\
                A detailed and well-structured OSINT report for the company, including sections on Company Information, Website Analysis, Domain and Network Analysis, Social Media and Contact Information, Search Engine Intelligence, Business Information, Regulatory and Legal Information, Technical Footprint, Intellectual Property, Employee and Hiring Information, Community and Public Perception, and Dark Web Mentions."""),
      agent=agent
    )