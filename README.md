# Reglex Models

This repository contains Pydantic models and prompts for extracting regulatory duties from UK legislation, specifically focused on local authority obligations.

## Contents

### Models (`models.py`)
- **Duty**: Complete model for regulatory duties placed on local authorities
- **ShouldExtractDuty**: Decision model for determining whether a regulation contains extractable duties
- **Themes**: Model for grouping related duties into thematic categories

### Prompts (`prompts.py`)
- **SHOULD_EXTRACT_DUTY_PROMPT**: Determines whether a regulation contains extractable duties
- **EXTRACT_DUTY_PROMPT**: Extracts detailed duty information from regulations
- **SUMMARY_PROMPT**: Summarizes high-level themes and requirements from statutory instruments

## Purpose

This system helps analyze UK statutory instruments to identify and categorize regulatory obligations placed on local authorities, enabling burden assessment and policy analysis.