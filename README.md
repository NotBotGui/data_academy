# BI & Data Learning Group

A shared repository for the BI and data learning group. We explore data engineering,
analytics, and visualisation using the **Contoso** sample datasets as a common foundation.

The stack covers **SQL Server**, **Power BI** (PBIP format), **Python**, **Jupyter notebooks**,
and **Streamlit** applications.

---

## Prerequisites

| Tool | Purpose |
|------|---------|
| [SQL Server](https://www.microsoft.com/en-us/sql-server/sql-server-downloads) (Express or Developer) | Local database engine |
| [SSMS](https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms) | One-time `.bacpac` import only |
| [VS Code](https://code.visualstudio.com/) + recommended extensions (see `.vscode/extensions.json`) | Primary editor |
| [Git](https://git-scm.com/) | Version control |
| [Python 3.10+](https://www.python.org/) | Scripts, notebooks, and Streamlit apps |

---

## Folder Structure

```
data_academy/
├── powerbi/
│   └── shared-assets/
│       ├── themes/          # JSON theme files
│       └── custom-visuals/  # .pbiviz files
│                            # PBIP projects go directly under powerbi/
│                            # Power BI Desktop manages internal structure
├── database/
│   ├── imported/            # Existing databases loaded via .bacpac
│   │   └── contoso-10k/
│   │       ├── bacpac/      # Source .bacpac file
│   │       ├── scripts/     # SQL exploration and modification scripts
│   │       └── migrations/  # Future versioned schema changes
│   ├── projects/            # Greenfield databases built from scratch (SSDT)
│   │   └── example-project/
│   │       ├── Tables/
│   │       ├── Views/
│   │       ├── StoredProcedures/
│   │       ├── Functions/
│   │       └── Scripts/     # Post-deployment and seed data scripts
│   └── backups/             # .bak files — excluded from Git
├── python/
│   ├── lib/                 # Shared installable internal packages
│   │   ├── db-connector/    # SQL Server and Snowflake connection helpers
│   │   └── pbi-utils/       # Power BI file and API helpers
│   └── projects/            # Standalone scripts and automations
│       └── example-project/ # Each project is self-contained
│           ├── src/
│           ├── notebooks/   # Notebooks live with their project
│           ├── pyproject.toml
│           └── requirements.txt
├── apps/
│   └── streamlit/
│       └── example-app/
│           ├── app.py
│           ├── pages/
│           ├── components/
│           ├── assets/
│           ├── notebooks/   # Prototyping notebooks for this app
│           ├── .streamlit/config.toml
│           └── requirements.txt
├── notebooks/               # Standalone exploration notebooks (SQL, Python, or mixed)
│                            # Notebooks tied to a project live inside that project folder
├── learning/                # Self-contained learning demos and exercises
│   └── 01_sales-analysis/   # Each topic in its own numbered subfolder
└── shared-assets/
    ├── datasets/            # Sample CSV or Excel reference files
    ├── templates/           # Reusable SQL query templates, script starters
    └── docs/                # Team documentation and onboarding guides
```

### Key distinctions

**`database/imported/` vs `database/projects/`**

- `database/imported/` is for **existing databases** (e.g. Contoso). Import the `.bacpac`
  via SSMS once, then use the `scripts/` folder for all SQL exploration and modifications.
- `database/projects/` is for **greenfield databases** built from scratch. Each subfolder
  is an SSDT project (`.sqlproj`) — schema as code, deployable from VS Code or the dotnet CLI.

**`python/lib/` vs `python/projects/`**

- `python/lib/` holds **shared internal packages** installed into any project via
  `pip install -e python/lib/<package>`. Code that is reused across multiple projects
  (database connections, API wrappers) belongs here.
- `python/projects/` holds **standalone scripts and automations** — each project is
  self-contained with its own virtual environment, dependencies, and notebooks.

**`notebooks/` vs project-level `notebooks/`**

- The top-level `notebooks/` folder is a **scratch space** for standalone explorations
  not yet tied to any project. Notebooks here can mix SQL and Python cells freely.
- Once a notebook matures into something reusable, move it into the relevant
  `python/projects/<project>/notebooks/` or `apps/streamlit/<app>/notebooks/` folder.

**`learning/` vs `python/projects/`**

- `learning/` is for **structured learning exercises** — numbered, self-contained, with
  a `README.md` explaining the objective. This is where group members commit and share
  their learning work.
- `python/projects/` is for **real automations and scripts** built for actual use.

---

## Getting Started

1. **Clone the repo**
   ```bash
   git clone <repo-url>
   cd data_academy
   ```

2. **Install recommended VS Code extensions**
   Open VS Code and accept the prompt, or run:
   ```
   Extensions: Show Recommended Extensions
   ```

3. **Set up notebook hygiene**
   Install `nbstripout` once after cloning. It will strip outputs before every commit
   (configured in `.gitattributes`):
   ```bash
   pip install nbstripout
   nbstripout --install
   ```

4. **Import the Contoso database**
   Open SSMS → right-click *Databases* → *Import Data-tier Application* → select the
   `.bacpac` file from `database/imported/contoso-10k/bacpac/`.

5. **Connect VS Code to SQL Server**
   Use the mssql extension (`Ctrl+Shift+P` → *MS SQL: Connect*) to connect to your
   local SQL Server instance and start running notebooks and scripts.

6. **Set up a Python project**
   Each project under `python/projects/` manages its own virtual environment locally:
   ```bash
   cd python/projects/example-project
   python -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

   To use a shared library from `python/lib/`:
   ```bash
   pip install -e ../../lib/db-connector
   ```

7. **Run a Streamlit app**
   ```bash
   cd apps/streamlit/example-app
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   streamlit run app.py
   ```

> Each project subfolder may contain its own `README.md` with more specific instructions.
