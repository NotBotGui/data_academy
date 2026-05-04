# BI & Data Learning Group

A shared repository for the BI and data learning group. We explore data engineering,
analytics, and visualisation using the **Contoso** sample datasets as a common foundation.

The stack covers **SQL Server**, **Power BI** (PBIP format), **Python**, **Jupyter notebooks**,
and **Streamlit** applications.

---

## Prerequisites

| Tool | Purpose |
|------|---------|
| [SQL Server](https://www.microsoft.com/en-us/sql-server/sql-server-downloads) (Express or Developer edition) | Local database engine |
| [SSMS](https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms) | One-time `.bacpac` import only |
| [VS Code](https://code.visualstudio.com/) + recommended extensions (see `.vscode/extensions.json`) | Primary editor for SQL, Python, and notebooks |
| [Git](https://git-scm.com/) | Version control |
| [Python 3.10+](https://www.python.org/) | Scripts and Streamlit apps |

---

## Folder Structure

```
data_academy/
├── powerbi/
│   ├── projects/          # Individual Power BI projects (PBIP format)
│   └── shared-assets/
│       ├── themes/        # JSON theme files
│       ├── custom-visuals/# .pbiviz files
│       └── shared-measures/
├── database/
│   ├── imported/          # Existing databases brought in via .bacpac
│   │   └── contoso-10k/
│   │       ├── bacpac/    # Source .bacpac file
│   │       ├── scripts/   # DDL, DML, stored procedures, exploration queries
│   │       └── migrations/# Future versioned schema changes
│   ├── projects/          # Greenfield databases built from scratch (SSDT)
│   │   └── example-project/
│   │       ├── Tables/
│   │       ├── Views/
│   │       ├── StoredProcedures/
│   │       ├── Functions/
│   │       └── Scripts/   # Post-deployment and seed data scripts
│   └── backups/           # .bak files — excluded from Git
├── python/
│   ├── scripts/           # Standalone scripts not tied to any app
│   ├── envs/              # Virtual environments — excluded from Git
│   └── requirements/      # requirements.txt files per project/use-case
├── notebooks/
│   ├── sql/               # SQL notebooks (.ipynb via mssql VS Code extension)
│   └── python/            # Python Jupyter notebooks
├── apps/
│   └── streamlit/
│       └── example-app/   # Each app in its own subfolder
│           ├── app.py
│           ├── pages/
│           ├── components/
│           ├── assets/
│           ├── data/
│           ├── .streamlit/config.toml
│           └── requirements.txt
├── use-cases/             # Structured learning exercises and proofs of concept
│   └── 01_sales-analysis/
└── shared-assets/
    ├── datasets/          # Sample CSV / Excel files
    ├── templates/         # Reusable query and script templates
    └── docs/              # Team documentation and onboarding guides
```

### Key distinctions

**`database/imported/` vs `database/projects/`**

- `database/imported/` is for **existing databases** that already exist (e.g. Contoso).
  You restore them by importing a `.bacpac` file into SQL Server via SSMS, then add
  scripts to document and query the schema.
- `database/projects/` is for **greenfield databases** built from scratch. Each subfolder
  is an **SSDT project** (`.sqlproj`) that defines the schema as code and can be deployed
  directly from VS Code or the dotnet CLI.

**`python/` vs `apps/streamlit/`**

- `python/` holds **standalone scripts** — one-off data processing, automation, or
  analysis files that are run directly and don't need a web interface.
- `apps/streamlit/` holds **deployable applications** — each subfolder is a self-contained
  Streamlit app with its own dependencies and configuration, intended to be shared or hosted.

---

## Getting Started

1. **Clone the repo**
   ```bash
   git clone <repo-url>
   cd data_academy
   ```

2. **Explore a use case**
   Navigate to `use-cases/` and open one of the numbered folders. Each contains a
   `README.md` that explains the objective and lists the relevant files.

3. **Set up a Streamlit app**
   ```bash
   cd apps/streamlit/example-app
   python -m venv ../../envs/example-app
   source ../../envs/example-app/bin/activate  # Windows: ...Scripts\activate
   pip install -r requirements.txt
   streamlit run app.py
   ```

4. **Work with the database**
   - To import Contoso: open SSMS, right-click *Databases → Import Data-tier Application*,
     and point it at the `.bacpac` file in `database/imported/contoso-10k/bacpac/`.
   - To work with an SSDT project: open the `.sqlproj` in VS Code with the mssql extension.

> Each project subfolder may contain its own `README.md` with more specific instructions.
