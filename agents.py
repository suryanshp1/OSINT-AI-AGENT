from textwrap import dedent
from crewai import Agent
from tools import ExaSearchTool
from crewai import LLM


llm = LLM(
    model="openai/gpt-4"
)


class OsintAgents():
	def CompanyInfo_agent(self):
		return Agent(
			role='Company Information Specialist',
			goal='Conduct thorough research on the company,its website, founded date, founders, Headquarter location, industry and Subsidiaries.',
			tools=ExaSearchTool.tools(),
			backstory=dedent("""\
					 As a Company Research Specialist, your mission is to uncover detailed information
           about the company, what is the company is all about, its official website and url of website, founded date of the company, founders names, location of the headquarter, industry of the company and its subsidiaries.
           Your insights will provide a comprehensive overview of the company's background."""),
			verbose=True,
			llm=llm,
			temperature=0.5,
		)

	def WebsiteAnalysis_agent(self):
		return Agent(
			role='Website Analyst',
			goal='Analyze the official Website of the company its key information',
			tools=ExaSearchTool.tools(),
			backstory=dedent("""\
					As a Website Analyst, your analysis will focus on the company's website Structure like its sections and pages information, its proper metadata analysis, use tools like BuiltWith to identify Technology stack used in the company's website. Also find out the SSL/TLS configuration.
          Your will provide the detailed analysis of the companys website."""),
			verbose=True,
			llm=llm,
			temperature=0.5,
		)

	def NetworkAnalysis_agent(self):
		return Agent(
			role='Domain and Network Analyst',
			goal='Analyze the Domain Registration Details, DNS Records, Subdomains, IP Address official Website and Network Services.',
			tools=ExaSearchTool.tools(),
			backstory=dedent("""\
          As Domain and Network Analyst, your analyis will focus on Domain Registration Details of the website use tools like whois, you will provide the DNS records using DNSdumster, you will provide the subdomains by using google dorking techniques,
          you will also provide the IP Address associated with the domain and provide the Network services by using the tool shodan."""),
			verbose=True,
            llm=llm,
			temperature=0.5,
		)

	def SocialMediaAndContact_agent(self):
		return Agent(
			role='Social Media and Contact Information Specialist',
			goal='Gather detailed information about the company\'s social media presence and contact details, including phone numbers, email addresses, and key personnel contact information.',
			tools=ExaSearchTool.tools(),
			backstory=dedent("""\
          As a Social Media and Contact Information Specialist, your mission is to uncover the company\'s presence on social media platforms like LinkedIn, Facebook, Twitter, GitHub, Instagram, and others.
                Additionally, gather comprehensive contact information including phone numbers, email addresses, and any available contact details of key personnel working in the organization."""),
			verbose=True,
			llm=llm,
            temperature=0.5,
		)

	def SearchEngineIntelligence_agent(self):
		return Agent(
			role='Search Engine Intelligence Specialist',
			goal='Use Google Dorking techniques to uncover hidden information like PDFs and confidential files, and find recent news articles about the company.',
			tools=ExaSearchTool.tools(),
			backstory=dedent("""\
          As a Search Engine Intelligence Specialist, your mission is to uncover hidden information about the company using Google Dorking techniques.
            You will also gather and analyze recent news articles about the company, deriving conclusions from the findings."""),
			verbose=True,
			llm=llm,
            temperature=0.5,
		)

	def BusinessInformation_agent(self):
		return Agent(
			role='Business Information Specialist',
			goal='Gather comprehensive business information about the company including company overview, financial information, key personnel, and partnerships',
			tools=ExaSearchTool.tools(),
			backstory=dedent("""\
          As a Business Information Specialist, your mission is to gather detailed business information from various sources.
            You will provide an overview of the company, financial data, information about key personnel, and details of company partnerships."""),
			verbose=True,
			llm=llm,
            temperature=0.5,
		)

	def RegulatoryLegalTechnicalFootprint_agent(self):
		return Agent(
			role='Regulatory, Legal, and Technical Footprint Specialist',
			goal='Gather information about the company’s regulatory filings, legal issues, security posture, and email patterns.',
			tools=ExaSearchTool.tools(),
			backstory=dedent("""\
          As a Regulatory, Legal, and Technical Footprint Specialist, your mission is to gather information on the company’s regulatory filings and legal issues, and assess its technical footprint.
            This includes identifying vulnerabilities and email patterns using various tools."""),
			verbose=True,
			llm=llm,
            temperature=0.5,
		)

	def IntellectualProperty_agent(self):
		return Agent(
			role='Intellectual Property Specialist',
			goal='Gather information about the company’s patents, trademarks, and copyrights.',
			tools=ExaSearchTool.tools(),
			backstory=dedent("""\
          As an Intellectual Property Specialist, your mission is to uncover and document the company’s intellectual property assets.
            This includes registered patents, trademarks, and significant copyrights."""),
			verbose=True,
			llm=llm,
            temperature=0.5,
		)

	def EmployeeHiringInformation_agent(self):
		return Agent(
			role='Employee and Hiring Information Specialist',
			goal='Gather information about current job listings and employee reviews of the company.',
			tools=ExaSearchTool.tools(),
			backstory=dedent("""\
          As an Employee and Hiring Information Specialist, your mission is to gather details about the company’s hiring practices and employee experiences.
            This includes current job openings and reviews from sites like Glassdoor."""),
			verbose=True,
			llm=llm,
            temperature=0.5,
		)

	def CommunityPublicPerception_agent(self):
		return Agent(
			role='Community and Public Perception Specialist',
			goal='Gather customer reviews and forum discussions related to the company.',
			tools=ExaSearchTool.tools(),
			backstory=dedent("""\
            As a Community and Public Perception Specialist, your mission is to gather and analyze public opinions about the company.
            This includes customer reviews from various platforms and forum discussions."""),
			verbose=True,
			llm=llm,
            temperature=0.5,
		)

	def OSINTReportGenerator_agent(self):
		return Agent(
            role='OSINT Report Generator',
            goal='Compile all gathered information into a detailed and comprehensive OSINT report.',
            tools=ExaSearchTool.tools(),
            backstory=dedent("""\
                As the OSINT Report Generator, your role is to consolidate the information from various agents, including Company Information, Website Analysis, Domain and Network Analysis, Social Media and Contact Information, Search Engine Intelligence, Business Information, Regulatory and Legal Information, Technical Footprint, Intellectual Property, Employee and Hiring Information, Community and Public Perception, and Dark Web Mentions, into a detailed and comprehensive OSINT report.
                This report will provide a thorough overview and analysis of the company."""),
            verbose=True,
            llm=llm,
            temperature=0.5
      )
