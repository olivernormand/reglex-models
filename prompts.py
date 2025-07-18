SHOULD_EXTRACT_DUTY_PROMPT = """
You are an expert at deciding whether there is a duty in the provided piece of regulations. You will need to decide whether there is a duty that needs to be extracted or not.

**Goal**: Determine whether the regulation describes a duty that needs to be extracted.

It's better to extract extra duties that can be manually reviewed than to miss important ones. Your primary goal in this step is to ensure that you do not miss any important duties. Government analysts will review and refine your extractions, so err on the side of inclusion rather than exclusion.

## Key Principles
You should only extract a duty if it is placing a demand on a local authority. If it is not, then you should not extract it. In your reasoning, make sure you explain why you're extracting the duty or why you're not.

Duties on a local authority include:
1. A requirement for the local authority to do something.
2. A requirement for an employee within the local authority to do something.
3. A conditional requirement for a local authority or employee to do something.
3. An expansion of existing responsibilities of the local authority to additional people or categories.

Duties on a local authority do not include:
1. Definitional statements
2. Interpretation of terms and references within the legislation

###### Read the explanatory note first
This often provides the clearest summary of what duties are contained in the legislation and will help you understand the context of the specific regulation.

###### If in doubt, extract the duty
Sometimes you many not be sure whether there is a duty in the provided regulations. If you're not confident, then extract the duty.

###### Look for additions to existing duties
Some SIs add people to groups that authorities already have responsibilities for, rather than creating entirely new duties. You should still flag these as duties.

<legislation>
{legislation}
</legislation>

<regulation>
{regulation}
</regulation>

Please determine whether there is a duty in the regulation.
"""

EXTRACT_DUTY_PROMPT = """
You are an expert at extracting duties from a piece of legislation. You will be provided with the entire legislation, and the specific regulation that you must extract your duty from.

**Goal**: Extract the duty from the regulation to a high quality.

#### Extract the duty in the context of the entire legislation
The duty you extract should be understandable as a standalone text. It should be a clear and concise description of the duty that contains all necessary context and details but no more. It should be understandable by a non-expert. Even if the duty references other legislation you should ensure the description is comprehensive and clear by itself.To ensure this is the case, you should ensure you understand the context of the full legislation and the duty within that.

#### One regulation may contain multiple duties
It is possible that a single regulation may contain multiple duties, this can happen only when there are multiple distinct duties within the same regulation. If this is the case then you should extract all the duties in the regulation as distinct duties. If this is not the case, then you should only extract the single duty. Unless there is obviously good reason to do otherwise, you should not extract multiple duties from a single regulation.

#### Common Challenges
- **SI is updating existing legislation** - Often an SI will update existing legislation. Again, ensure you understand the context but in your duty description make sure you summarise the impact of the change to the local authority, rather than just repeating what the update is. 
- **Vague or complex language** - Summarize clearly while preserving important detail
- **References to other legislation** - Include these references in your description rather than trying to look up the base legislation


<legislation>
{legislation}
</legislation>

<regulation>
{regulation}
</regulation>
Please extract the duty from the regulation.
"""


SUMMARY_PROMPT = """
You are an expert at summarising the main asks of a local authority from a Statutory Instrument. You will be given a piece of legislation and you will need to summarise the main asks of the local authority.

**Goal**: Summarise the asks this duty places on the local authority.

## Background
The provided legislation has already been analysed in detail to understand what the individual duties being placed on local authorities are. In addition, these duties have been extracted to a high quality. In addition to this granular extraction, you will need to provide a complete but concise summary of the main asks of the local authority contained within the legislation.

This is therefore a chance to pull out the high level themes that capture the main themes and essence of the regulatory burdens.

## Key Principles

As part of this extraction process you should focus on the following:
**High level themes** - The main asks or burdens being placed on local authorities.
**Summary of core requirements** - The big picture of what an SI is requiring, not the detailed implementation.
**Main essence capture** - The primary regulatory themes rather than every sub-regulation.

You should not attempt to do the following:
**Granular detail** - You should not attempt to capture the granular detail of the individual duties, this has already been done and would not add additional value.
**Exhaustive mapping** - You should not attempt to capture everything at the regulation-by-regulation level.
**Implementation specifics** - You should not attempt to capture details like "set this up within five working days" and similar procedural minutiae.

## Mapping of existing duties
In addition to being provided with the legislation, you will also be provided with the duties that have already been extracted. After you have summarised the main asks of the local authority, you should map these to the duties that have already been extracted. Only map duties that are clearly related to the main asks of the local authority. If there are duties that are not directly related to the main asks of the local authority, then you should not map them. It is okay for there to be duties that are not mapped to the main asks of the local authority.

<legislation>
{legislation}
</legislation>

<duties>
{duties}
</duties>

Please summarise the main asks of the local authority.
"""
