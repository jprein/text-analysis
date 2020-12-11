library(reticulate)
os <- import("os")
os$listdir(".")

# use_python("/usr/local/bin/python")

# install libraries that aren't installed yet (whhich are in the .py file)
run_python_file <- function(python_file){
  a = try(reticulate::py_run_file(python_file),silent=TRUE)
  if(inherits(a,"try-error")& grepl("ModuleNotFoundError",a)){
    system(sprintf("python -m pip install %s",gsub(".* |\\W","",c(a))))
    run_python_file(python_file)
  }
  else a
}
run_python_file("pdfconverter.py")

source_python("pdfconverter.py")
tmp <- convert_pdf_to_txt("/Users/julia_prein/Work/experiments/soc_cog_textanalysis/doc/testpdf.pdf")

write.table(tmp,"test.txt", col.names = FALSE, row.names = FALSE, sep = "\n")
