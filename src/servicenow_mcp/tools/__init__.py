"""
Tools module for the ServiceNow MCP server.
"""

# Import tools as they are implemented
from servicenow_mcp.tools.incident_tools import (
    add_comment,
    create_incident,
    list_incidents,
    resolve_incident,
    update_incident,
)
from servicenow_mcp.tools.knowledge_base import (
    create_article,
    create_category,
    create_knowledge_base,
    get_article,
    list_articles,
    list_knowledge_bases,
    publish_article,
    update_article,
    list_categories,
)
# from servicenow_mcp.tools.problem_tools import create_problem, update_problem
# from servicenow_mcp.tools.request_tools import create_request, update_request

__all__ = [
    # Incident tools
    "create_incident",
    "update_incident",
    "add_comment",
    "resolve_incident",
    "list_incidents",
    
        
    # Knowledge Base tools
    "create_knowledge_base",
    "list_knowledge_bases",
    "create_category",
    "list_categories",
    "create_article",
    "update_article",
    "publish_article",
    "list_articles",
    "get_article",

] 