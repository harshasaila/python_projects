function main(workbook: ExcelScript.Workbook) {
    // Configurable parameters
    const targetAssignedTo: string = "Harsha"; // Replace with actual target filter name
    const checkedByName: string = "Name2";  // Replace with actual checker name
    const password: string = "12345";

    // 1. Keep only 'After production' or the first sheet; delete all others
    let targetSheet: ExcelScript.Worksheet | undefined = workbook.getWorksheet("After production");
    if (!targetSheet) {
        targetSheet = workbook.getWorksheets()[0];
    }

    const allSheets: ExcelScript.Worksheet[] = workbook.getWorksheets();
    for (let i: number = allSheets.length - 1; i >= 0; i--) {
        if (allSheets[i].getId() !== targetSheet.getId()) {
            allSheets[i].delete();
        }
    }

    // 2. Unprotect, Unfreeze, and Remove AutoFilter at the start
    try {
        targetSheet.getProtection().unprotect(password);
    } catch (e) {
        // Continue if already unprotected
    }

    targetSheet.getFreezePanes().unfreeze();

    if (targetSheet.getAutoFilter()) {
        targetSheet.getAutoFilter().remove();
    }

    // 3. Get Used Range and convert error indicators directly on the original sheet
    const usedRange: ExcelScript.Range | undefined = targetSheet.getUsedRange();
    if (!usedRange) return;

    const rawValues: (string | number | boolean)[][] = usedRange.getValues();
    const rowCount: number = rawValues.length;
    const colCount: number = rawValues[0].length;

    // Convert stored-as-text numbers into pure numbers
    for (let r: number = 0; r < rowCount; r++) {
        for (let c: number = 0; c < colCount; c++) {
            const val: string | number | boolean = rawValues[r][c];
            if (typeof val === "string" && val.trim() !== "" && !isNaN(Number(val))) {
                rawValues[r][c] = Number(val);
            }
        }
    }

    // Explicitly write converted numeric values back to target sheet
    usedRange.setValues(rawValues);

    // 4. Map Header Columns
    const headers: string[] = rawValues[0].map((h: string | number | boolean) => String(h).trim().toLowerCase());
    const assignedToIdx: number = headers.indexOf("assigned to");

    if (assignedToIdx === -1) return;

    // 5. Filter rows matching assigned name
    const filteredRows: (string | number | boolean)[][] = [rawValues[0]];

    for (let r: number = 1; r < rowCount; r++) {
        if (String(rawValues[r][assignedToIdx]).toLowerCase() === targetAssignedTo.toLowerCase()) {
            filteredRows.push(rawValues[r]);
        }
    }

    if (filteredRows.length <= 1) return;

    // 6. Re-create Sheet1 cleanly
    let sheet1: ExcelScript.Worksheet | undefined = workbook.getWorksheet("Sheet1");
    if (sheet1) {
        sheet1.delete();
    }
    sheet1 = workbook.addWorksheet("Sheet1");

    // Map header indexes for Sheet1 logic
    const s1Headers: string[] = filteredRows[0].map((h: string | number | boolean) => String(h).trim().toLowerCase());
    const checkedByIdx: number = s1Headers.indexOf("checked by");
    const pnrrIdx: number = s1Headers.indexOf("pnrr");
    const timeTakenIdx: number = s1Headers.indexOf("time taken in minutes");
    const activeLinesIdx: number = s1Headers.indexOf("active lines");
    const rbsIdx: number = s1Headers.indexOf("rbs");
    const addressIdx: number = s1Headers.indexOf("address details change");
    const feedbackIdx: number = s1Headers.indexOf("feedback");

    // 7. Process row updates in memory
    for (let r: number = 1; r < filteredRows.length; r++) {
        const row: (string | number | boolean)[] = filteredRows[r];

        if (checkedByIdx !== -1) {
            row[checkedByIdx] = checkedByName;
        }

        if (pnrrIdx !== -1 && timeTakenIdx !== -1) {
            const pnrrVal: string | number | boolean = row[pnrrIdx];
            if (pnrrVal === 1 || pnrrVal === 0 || pnrrVal === "1" || pnrrVal === "0") {
                row[timeTakenIdx] = 3;
            } else if (pnrrVal === "" || pnrrVal === null || pnrrVal === undefined) {
                row[timeTakenIdx] = 6;
            }
        }

        if (feedbackIdx !== -1) {
            if (activeLinesIdx !== -1 && (row[activeLinesIdx] === 1 || row[activeLinesIdx] === "1")) {
                row[feedbackIdx] = "ACT";
            }
            if (rbsIdx !== -1 && (row[rbsIdx] === 1 || row[rbsIdx] === "1")) {
                row[feedbackIdx] = "RBS";
            }
            if (addressIdx !== -1 && (row[addressIdx] === 1 || row[addressIdx] === "1")) {
                row[feedbackIdx] = "ADR";
            }
        }
    }

    // 8. Append filename + "_Harsha" at bottom of "Assigned To" column
    const wbName: string = workbook.getName().replace(/\.[^/.]+$/, "");
    const appendedRow: (string | number | boolean)[] = new Array(colCount).fill("");
    appendedRow[assignedToIdx] = `${wbName}_Harsha`;
    filteredRows.push(appendedRow);

    // 9. Write data into Sheet1
    const targetRange: ExcelScript.Range = sheet1.getRangeByIndexes(0, 0, filteredRows.length, colCount);
    targetRange.setValues(filteredRows);

    // 10. Format Header Row as Bold
    const headerRange: ExcelScript.Range = sheet1.getRangeByIndexes(0, 0, 1, colCount);
    headerRange.getFormat().getFont().setBold(true);

    // 11. Activate Sheet1 and set tab orders
    sheet1.setPosition(0);
    targetSheet.setPosition(1);
    sheet1.activate();

    // // 12. Freeze Top Row (Row 1) and Columns A through D
    // sheet1.getFreezePanes().freezeAt("E2");

    // // 13. Select A1 first to align Row 1, then E2 to align Column E
    // sheet1.getRange("A1").select();
    // sheet1.getRange("E2").select();
}