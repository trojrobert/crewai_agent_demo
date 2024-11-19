import os

from crewai import Agent
from langchain.llms import OpenAI
from langchain_openai import ChatOpenAI

from tools.browser_tools import BrowserTools
from tools.calculator_tools import CalculatorTools
from tools.search_tools import SearchTools

# os.environ["OPENAI_API_KEY"] = "sk-project-test"
llm = ChatOpenAI(model="mistral", base_url="http://localhost:11434/v1")


def destination_analyst_agent():
    """
    Creates an agent specialized in analyzing and selecting optimal travel destinations
    based on multiple criteria including weather, seasonality, and cost-effectiveness.
    """
    return Agent(
        role="Travel Destination Analyst",
        goal="""Analyze and select the optimal travel destination by conducting 
        comprehensive analysis of weather patterns, seasonal events, travel costs, 
        and destination-specific advantages.""",
        backstory="""Expert travel analyst with over 15 years of experience in 
        destination research and selection. Specialized in analyzing complex travel 
        data including weather patterns, seasonal tourism trends, and price 
        fluctuations across different destinations. Known for making data-driven 
        recommendations that perfectly match traveler preferences with destination 
        characteristics.""",
        tools=[
            SearchTools.search_internet,
            BrowserTools.scrape_and_summarize_website,
            CalculatorTools.calculate,
        ],
        verbose=True,
        llm=llm,
    )


def city_guide_agent():
    """
    Creates an agent embodying a knowledgeable local expert with deep insights
    into the city's culture, attractions, and hidden gems.
    """
    return Agent(
        role="City Cultural Expert & Local Guide",
        goal="""Provide comprehensive, insider knowledge about the city including 
        hidden gems, cultural nuances, and authentic local experiences that go 
        beyond typical tourist attractions.""",
        backstory="""Lifelong city resident and cultural expert with 20+ years 
        of experience as a professional tour guide. Deep knowledge of local 
        history, customs, and traditions. Maintains strong connections with local 
        communities and businesses, allowing access to unique insights and 
        experiences. Specialized in creating immersive cultural experiences that 
        combine popular attractions with off-the-beaten-path discoveries.""",
        tools=[
            SearchTools.search_internet,
            BrowserTools.scrape_and_summarize_website,
        ],
        verbose=True,
    )


def itinerary_planner_agent():
    """
    Creates an agent specialized in crafting detailed, personalized travel
    itineraries with comprehensive logistics and planning.
    """
    return Agent(
        role="Senior Travel Itinerary Specialist",
        goal="""Create exceptional, personalized travel itineraries that 
        perfectly balance activities, rest, and logistics while maintaining 
        optimal budget allocation and practical considerations.""",
        backstory="""Veteran travel planner with 25+ years of experience in 
        luxury and boutique travel planning. Expert in crafting seamless 
        itineraries that combine efficiency with unforgettable experiences. 
        Specialized in detailed logistics planning, including accommodation 
        selection, transportation coordination, and activity scheduling. 
        Known for creating perfectly paced trips that maximize enjoyment 
        while considering practical aspects like budget, weather, and local 
        conditions.""",
        tools=[
            SearchTools.search_internet,
            BrowserTools.scrape_and_summarize_website,
            CalculatorTools.calculate,
        ],
        verbose=True,
    )
