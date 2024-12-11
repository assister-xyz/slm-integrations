# ASSISTERR Documentation

### How to login to Assisterr?
`https://assisterr.gitbook.io/assisterr/product-guides/login-slm-store`
### How to find SLM's on Assisterr?
`https://assisterr.gitbook.io/assisterr/product-guides/slm-store`
### How to create your own SLM?
`https://assisterr.gitbook.io/assisterr/product-guides/create-your-first-slm`
### How to integrate SLM with API?
`https://assisterr.gitbook.io/assisterr/product-guides/assisterr-slm-integration`

---

# API Documentation

## Base URL
`https://api.assisterr.ai/`

---

## Endpoints

### 1. [POST] /api/v1/slm/{handle_name}/chat/
**Description:** Request to receive a response from SLM without context binding (without keeping history).

**Headers:**
| Header       | Required | Example Value                                         | Description                |
|--------------|----------|-------------------------------------------------------|----------------------------|
| `X-Api-Key`  | Yes      | `your_token`                                          | API Key for authentication.|

**Path Parameters:**
| Parameter      | Type   | Required | Description                       |
|----------------|--------|----------|-----------------------------------|
| `handle_name`  | string | Yes      | Unique identifier for the slm.    |

**Request Body (JSON):**
```json
{
  "query": "Your query here"
}
```

### 2. [POST] /api/v1/slm/{handle_name}/chat/stream/
**Description:** Request to receive a stream (SSE) response from SLM without context binding (without keeping history).

**Headers:**
| Header       | Required | Example Value        | Description                |
|--------------|----------|----------------------|----------------------------|
| `X-Api-Key`  | Yes      | `your_token`         | API Key for authentication.|

**Path Parameters:**
| Parameter      | Type   | Required | Description                       |
|----------------|--------|----------|-----------------------------------|
| `handle_name`  | string | Yes      | Unique identifier for the slm.    |

**Request Body (JSON):**
```json
{
  "query": "Your query here"
}
```

### 3. [POST] /api/v1/slm/{handle_name}/session/create/
**Description:** Request to receive a session ID.

**Headers:**
| Header       | Required | Example Value        | Description                |
|--------------|----------|----------------------|----------------------------|
| `X-Api-Key`  | Yes      | `your_token`         | API Key for authentication.|

**Path Parameters:**
| Parameter      | Type   | Required | Description                       |
|----------------|--------|----------|-----------------------------------|
| `handle_name`  | string | Yes      | Unique identifier for the slm.    |

**Respponse Body (JSON):**
```json
"1234567891234"
```


### 4. [POST] /api/v1/slm/{handle_name}/session/{slm_session_id}/chat/
**Description:** Request to receive a response from SLM with context binding (with keeping history).

**Headers:**
| Header       | Required | Example Value                                         | Description                |
|--------------|----------|-------------------------------------------------------|----------------------------|
| `X-Api-Key`  | Yes      | `your_token`                                          | API Key for authentication.|

**Path Parameters:**
| Parameter         | Type   | Required | Description                       |
|-------------------|--------|----------|-----------------------------------|
| `handle_name`     | string | Yes      | Unique identifier for the slm.    |
| `slm_session_id`  | string | Yes      | Unique session identifier.        |

**Request Body (JSON):**
```json
{
  "query": "Your query here"
}
```


### 5. [POST] /api/v1/slm/{handle_name}/session/{slm_session_id}/chat/stream
**Description:** Request to receive a stream (SSE) response from SLM with context binding (with keeping history).

**Headers:**
| Header       | Required | Example Value                                         | Description                |
|--------------|----------|-------------------------------------------------------|----------------------------|
| `X-Api-Key`  | Yes      | `your_token`                                          | API Key for authentication.|

**Path Parameters:**
| Parameter         | Type   | Required | Description                       |
|-------------------|--------|----------|-----------------------------------|
| `handle_name`     | string | Yes      | Unique identifier for the slm.    |
| `slm_session_id`  | string | Yes      | Unique session identifier.        |

**Request Body (JSON):**
```json
{
  "query": "Your query here"
}
```


### 6. [GET] /api/v1/slm/{handle_name}/session/list/
**Description:** Request to receive a list of all sessions.

**Headers:**
| Header       | Required | Example Value                                         | Description                |
|--------------|----------|-------------------------------------------------------|----------------------------|
| `X-Api-Key`  | Yes      | `your_token`                                          | API Key for authentication.|

**Path Parameters:**
| Parameter         | Type   | Required | Description                       |
|-------------------|--------|----------|-----------------------------------|
| `handle_name`     | string | Yes      | Unique identifier for the slm.    |
| `slm_session_id`  | string | Yes      | Unique session identifier.        |



### 7. [GET] /api/v1/slm/{handle_name}/session/{slm_session_id}/history/
**Description:** Request to receive a conversation of session.

**Headers:**
| Header       | Required | Example Value                                         | Description                |
|--------------|----------|-------------------------------------------------------|----------------------------|
| `X-Api-Key`  | Yes      | `your_token`                                          | API Key for authentication.|

**Path Parameters:**
| Parameter         | Type   | Required | Description                       |
|-------------------|--------|----------|-----------------------------------|
| `handle_name`     | string | Yes      | Unique identifier for the slm.    |
| `slm_session_id`  | string | Yes      | Unique session identifier.        |


### 8. [DELETE] /api/v1/slm/{handle_name}/session/{slm_session_id}/
**Description:** Delete session

**Headers:**
| Header       | Required | Example Value                                         | Description                |
|--------------|----------|-------------------------------------------------------|----------------------------|
| `X-Api-Key`  | Yes      | `your_token`                                          | API Key for authentication.|

**Path Parameters:**
| Parameter         | Type   | Required | Description                       |
|-------------------|--------|----------|-----------------------------------|
| `handle_name`     | string | Yes      | Unique identifier for the slm.    |
| `slm_session_id`  | string | Yes      | Unique session identifier.        |


---

# Examples

Examples folder contains examples notebooks on how to use Assisterr SLMs.
From Basic API usage to SLM as agent like Automatic X poster or Solana onchain bot.
