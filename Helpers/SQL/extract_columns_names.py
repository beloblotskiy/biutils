import re

sql = """    EFFDT              DATE NOT NULL ,
    EFFSEQ             NUMBER (*,0) NOT NULL ,
    PER_ORG            VARCHAR2 (3 BYTE) NOT NULL ,
    POSITION_NBR       VARCHAR2 (8 BYTE) NOT NULL ,
    SUPERVISOR_ID      VARCHAR2 (11 BYTE) NOT NULL ,
    HR_STATUS          VARCHAR2 (1 BYTE) NOT NULL ,
    APPT_TYPE          VARCHAR2 (1 BYTE) NOT NULL ,
    MAIN_APPT_NUM_JPN  NUMBER (*,0) NOT NULL ,
    POSITION_OVERRIDE  VARCHAR2 (1 BYTE) NOT NULL ,
    POSN_CHANGE_RECORD VARCHAR2 (1 BYTE) NOT NULL ,
    EMPL_STATUS        VARCHAR2 (1 BYTE) NOT NULL ,
    ACTION             VARCHAR2 (3 BYTE) NOT NULL ,
    ACTION_DT          DATE ,
    ACTION_REASON      VARCHAR2 (3 BYTE) NOT NULL ,
    TAX_LOCATION_CD    VARCHAR2 (10 BYTE) NOT NULL ,
    JOB_ENTRY_DT       DATE ,
    DEPT_ENTRY_DT      DATE ,
    POSITION_ENTRY_DT  DATE ,
    SHIFT              VARCHAR2 (1 BYTE) NOT NULL ,
    REG_TEMP           VARCHAR2 (1 BYTE) NOT NULL ,
    FULL_PART_TIME     VARCHAR2 (1 BYTE) NOT NULL ,
    COMPANY            VARCHAR2 (3 BYTE) NOT NULL ,
    PAYGROUP           VARCHAR2 (3 BYTE) NOT NULL ,
    BAS_GROUP_ID       VARCHAR2 (3 BYTE) NOT NULL ,
    ELIG_CONFIG1       VARCHAR2 (10 BYTE) NOT NULL ,
    ELIG_CONFIG2       VARCHAR2 (10 BYTE) NOT NULL ,
    ELIG_CONFIG3       VARCHAR2 (10 BYTE) NOT NULL ,
    ELIG_CONFIG4       VARCHAR2 (10 BYTE) NOT NULL ,
    ELIG_CONFIG5       VARCHAR2 (10 BYTE) NOT NULL ,
    ELIG_CONFIG6       VARCHAR2 (10 BYTE) NOT NULL ,
    ELIG_CONFIG7       VARCHAR2 (10 BYTE) NOT NULL ,
    ELIG_CONFIG8       VARCHAR2 (10 BYTE) NOT NULL ,
    ELIG_CONFIG9       VARCHAR2 (10 BYTE) NOT NULL ,
    BEN_STATUS         VARCHAR2 (4 BYTE) NOT NULL ,
    BAS_ACTION         VARCHAR2 (3 BYTE) NOT NULL ,
    COBRA_ACTION       VARCHAR2 (3 BYTE) NOT NULL ,
    EMPL_TYPE          VARCHAR2 (1 BYTE) NOT NULL ,
    HOLIDAY_SCHEDULE   VARCHAR2 (6 BYTE) NOT NULL ,
    STD_HOURS          NUMBER (6,2) NOT NULL ,
    STD_HRS_FREQUENCY  VARCHAR2 (5 BYTE) NOT NULL ,
    OFFICER_CD         VARCHAR2 (1 BYTE) NOT NULL ,
    EMPL_CLASS         VARCHAR2 (3 BYTE) NOT NULL ,
    SAL_ADMIN_PLAN     VARCHAR2 (4 BYTE) NOT NULL ,
    GRADE              VARCHAR2 (3 BYTE) NOT NULL ,
    GRADE_ENTRY_DT     DATE ,
    STEP               NUMBER (*,0) NOT NULL ,
    STEP_ENTRY_DT      DATE ,
    GL_PAY_TYPE        VARCHAR2 (6 BYTE) NOT NULL ,
    ACCT_CD            VARCHAR2 (25 BYTE) NOT NULL ,
    EARNS_DIST_TYPE    VARCHAR2 (1 BYTE) NOT NULL ,
    COMP_FREQUENCY     VARCHAR2 (5 BYTE) NOT NULL ,
    COMPRATE           NUMBER (18,6) NOT NULL ,
    CHANGE_AMT         NUMBER (18,6) NOT NULL ,
    CHANGE_PCT         NUMBER (6,3) NOT NULL ,
    ANNUAL_RT          NUMBER (18,3) NOT NULL ,
    MONTHLY_RT         NUMBER (18,3) NOT NULL ,
    DAILY_RT           NUMBER (18,3) NOT NULL ,
    HOURLY_RT          NUMBER (18,6) NOT NULL ,
    ANNL_BENEF_BASE_RT NUMBER (18,3) NOT NULL ,
    SHIFT_RT           NUMBER (18,6) NOT NULL ,
    SHIFT_FACTOR       NUMBER (4,3) NOT NULL ,
    CURRENCY_CD        VARCHAR2 (3 BYTE) NOT NULL ,
    BUSINESS_UNIT      VARCHAR2 (5 BYTE) NOT NULL ,
    SETID_SALARY       VARCHAR2 (5 BYTE) NOT NULL ,
    SETID_EMPL_CLASS   VARCHAR2 (5 BYTE) NOT NULL ,
    REG_REGION         VARCHAR2 (5 BYTE) NOT NULL ,
    DIRECTLY_TIPPED    VARCHAR2 (1 BYTE) NOT NULL ,
    FLSA_STATUS        VARCHAR2 (1 BYTE) NOT NULL ,
    EEO_CLASS          VARCHAR2 (1 BYTE) NOT NULL ,
    FUNCTION_CD        VARCHAR2 (2 BYTE) NOT NULL ,
    TARIFF_GER         VARCHAR2 (2 BYTE) NOT NULL ,
    TARIFF_AREA_GER    VARCHAR2 (3 BYTE) NOT NULL ,
    PERFORM_GROUP_GER  VARCHAR2 (2 BYTE) NOT NULL ,
    LABOR_TYPE_GER     VARCHAR2 (1 BYTE) NOT NULL ,
    SPK_COMM_ID_GER    VARCHAR2 (9 BYTE) NOT NULL ,
    HOURLY_RT_FRA      VARCHAR2 (3 BYTE) NOT NULL ,
    ACCDNT_CD_FRA      VARCHAR2 (1 BYTE) NOT NULL ,
    VALUE_1_FRA        VARCHAR2 (5 BYTE) NOT NULL ,
    VALUE_2_FRA        VARCHAR2 (5 BYTE) NOT NULL ,
    VALUE_3_FRA        VARCHAR2 (5 BYTE) NOT NULL ,
    VALUE_4_FRA        VARCHAR2 (5 BYTE) NOT NULL ,
    VALUE_5_FRA        VARCHAR2 (5 BYTE) NOT NULL ,
    CTG_RATE           NUMBER (*,0) NOT NULL ,
    PAID_HOURS         NUMBER (6,2) NOT NULL ,
    PAID_FTE           NUMBER (7,6) NOT NULL ,
    PAID_HRS_FREQUENCY VARCHAR2 (5 BYTE) NOT NULL ,
    UNION_FULL_PART    VARCHAR2 (1 BYTE) NOT NULL ,
    UNION_POS          VARCHAR2 (1 BYTE) NOT NULL ,
    MATRICULA_NBR      NUMBER (*,0) NOT NULL ,
    SOC_SEC_RISK_CODE  VARCHAR2 (3 BYTE) NOT NULL ,
    UNION_FEE_AMOUNT   NUMBER (8,2) NOT NULL ,
    UNION_FEE_START_DT DATE ,
    UNION_FEE_END_DT   DATE ,
    EXEMPT_JOB_LBR     VARCHAR2 (1 BYTE) NOT NULL ,
    EXEMPT_HOURS_MONTH NUMBER (*,0) NOT NULL ,
    WRKS_CNCL_FUNCTION VARCHAR2 (1 BYTE) NOT NULL ,
    INTERCTR_WRKS_CNCL VARCHAR2 (1 BYTE) NOT NULL ,
    CURRENCY_CD1       VARCHAR2 (3 BYTE) NOT NULL ,
    PAY_UNION_FEE      VARCHAR2 (1 BYTE) NOT NULL ,
    UNION_CD           VARCHAR2 (3 BYTE) NOT NULL ,
    BARG_UNIT          VARCHAR2 (4 BYTE) NOT NULL ,
    UNION_SENIORITY_DT DATE ,
    ENTRY_DATE         DATE ,
    LABOR_AGREEMENT    VARCHAR2 (6 BYTE) NOT NULL ,
    EMPL_CTG           VARCHAR2 (6 BYTE) NOT NULL ,
    EMPL_CTG_L1        VARCHAR2 (6 BYTE) NOT NULL ,
    EMPL_CTG_L2        VARCHAR2 (6 BYTE) NOT NULL ,
    SETID_LBR_AGRMNT   VARCHAR2 (5 BYTE) NOT NULL ,
    WPP_STOP_FLAG      VARCHAR2 (1 BYTE) NOT NULL ,
    LABOR_FACILITY_ID  VARCHAR2 (10 BYTE) NOT NULL ,
    LBR_FAC_ENTRY_DT   DATE ,
    LAYOFF_EXEMPT_FLAG VARCHAR2 (1 BYTE) NOT NULL ,
    LAYOFF_EXEMPT_RSN  VARCHAR2 (11 BYTE) NOT NULL ,
    GP_PAYGROUP        VARCHAR2 (10 BYTE) NOT NULL ,
    GP_DFLT_ELIG_GRP   VARCHAR2 (1 BYTE) NOT NULL ,
    GP_ELIG_GRP        VARCHAR2 (10 BYTE) NOT NULL ,
    GP_DFLT_CURRTTYP   VARCHAR2 (1 BYTE) NOT NULL ,
    CUR_RT_TYPE        VARCHAR2 (5 BYTE) NOT NULL ,
    GP_DFLT_EXRTDT     VARCHAR2 (1 BYTE) NOT NULL ,
    GP_ASOF_DT_EXG_RT  VARCHAR2 (1 BYTE) NOT NULL ,
    ADDS_TO_FTE_ACTUAL VARCHAR2 (1 BYTE) NOT NULL ,
    CLASS_INDC         VARCHAR2 (1 BYTE) NOT NULL ,
    ENCUMB_OVERRIDE    VARCHAR2 (1 BYTE) NOT NULL ,
    FICA_STATUS_EE     VARCHAR2 (1 BYTE) NOT NULL ,
    FTE                NUMBER (7,6) NOT NULL ,
    PRORATE_CNT_AMT    VARCHAR2 (1 BYTE) NOT NULL ,
    PAY_SYSTEM_FLG     VARCHAR2 (2 BYTE) NOT NULL ,
    BORDER_WALKER      VARCHAR2 (1 BYTE) NOT NULL ,
    LUMP_SUM_PAY       VARCHAR2 (1 BYTE) NOT NULL ,
    CONTRACT_NUM       VARCHAR2 (25 BYTE) NOT NULL ,
    JOB_INDICATOR      VARCHAR2 (1 BYTE) NOT NULL ,
    WRKS_CNCL_ROLE_CHE VARCHAR2 (30 BYTE) NOT NULL ,
    BENEFIT_SYSTEM     VARCHAR2 (2 BYTE) NOT NULL ,
    WORK_DAY_HOURS     NUMBER (6,2) NOT NULL ,
    REPORTS_TO         VARCHAR2 (8 BYTE) NOT NULL ,
    FORCE_PUBLISH      DATE ,
    JOB_DATA_SRC_CD    VARCHAR2 (3 BYTE) NOT NULL ,
    ESTABID            VARCHAR2 (12 BYTE) NOT NULL ,
    SUPV_LVL_ID        VARCHAR2 (8 BYTE) NOT NULL ,
    SETID_SUPV_LVL     VARCHAR2 (5 BYTE) NOT NULL ,
    ABSENCE_SYSTEM_CD  VARCHAR2 (3 BYTE) NOT NULL ,
    POI_TYPE           VARCHAR2 (5 BYTE) NOT NULL ,
    HIRE_DT            DATE ,
    LAST_HIRE_DT       DATE ,
    TERMINATION_DT     DATE ,
    ASGN_START_DT      DATE ,
    LST_ASGN_START_DT  DATE ,
    ASGN_END_DT        DATE ,
    LDW_OVR            VARCHAR2 (1 BYTE) NOT NULL ,
    LAST_DATE_WORKED   DATE ,
    EXPECTED_RETURN_DT DATE ,
    EXPECTED_END_DATE  DATE ,
    AUTO_END_FLG       VARCHAR2 (1 BYTE) NOT NULL ,
    LASTUPDDTTM        TIMESTAMP ,
    LASTUPDOPRID       VARCHAR2 (30 BYTE) NOT NULL ,
    SETID_DEPT         VARCHAR2 (5 BYTE) NOT NULL ,
    DEPTID             VARCHAR2 (10 BYTE) NOT NULL ,
    SETID_LOCATION     VARCHAR2 (5 BYTE) NOT NULL ,
    LOCATION           VARCHAR2 (10 BYTE) NOT NULL ,
    SETID_JOBCODE      VARCHAR2 (5 BYTE) NOT NULL ,
    JOBCODE            VARCHAR2 (6 BYTE) NOT NULL ,
    EMPL_RCD           NUMBER (*,0) NOT NULL ,
    COL_2123           VARCHAR2 (11 BYTE) NOT NULL ,
    COL_2125           NUMBER (*,0) NOT NULL"""

fields = re.findall(r"^(?im)\s*(.*?)\s+.*$", sql)
print "\n".join(sorted(fields))